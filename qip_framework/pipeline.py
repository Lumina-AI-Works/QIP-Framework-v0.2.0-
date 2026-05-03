import numpy as np
from qiskit import transpile
from qiskit_aer import AerSimulator

from .encoding import encode_qpie, encode_frqi
from .algorithms import create_qhed_circuit, create_inversion_circuit, create_brightness_circuit, create_blur_circuit, create_dilation_circuit
from .noise import create_advanced_noise_model
from .analysis import calculate_cosine_similarity, calculate_ssim, reconstruct_from_counts, normalize_for_display
from .utils import load_and_preprocess, classical_baseline_sobel, is_power_of_two

class QIPPipeline:
    """
    Research-grade pipeline for Quantum Image Processing.
    
    This class orchestrates the entire workflow of encoding a classical image,
    applying a quantum algorithm, simulating hardware noise, and reconstructing
    the resulting image.
    
    Attributes:
        encoding_type (str): Type of image encoding ("qpie" or "frqi").
        algorithm_type (str): Quantum algorithm to apply ("qhed", "inversion", or "brightness").
        noise_config (dict): Configuration for the NISQ noise model.
    """
    def __init__(self, encoding: str = "qpie", algorithm: str = "qhed", noise_config: dict = None):
        self.encoding_type = encoding
        self.algorithm_type = algorithm
        self.noise_config = noise_config or {"p_gate": 0.01, "p_meas": 0.02}
        self.sim = AerSimulator()
        
    def _validate_image(self, img):
        """Strict validation for input images."""
        if not isinstance(img, np.ndarray):
            raise TypeError(f"Input must be a numpy ndarray, got {type(img)}")
        
        if len(img.shape) == 3:
            # Handle RGB by warning and converting to grayscale
            print("Warning: Input image has 3 channels. Converting to grayscale.")
            import cv2
            img_uint8 = (img * 255).astype(np.uint8)
            img = cv2.cvtColor(img_uint8, cv2.COLOR_BGR2GRAY) / 255.0
            
        if np.max(img) > 1.0 or np.min(img) < 0.0:
            raise ValueError("Pixel values must be normalized between 0.0 and 1.0")
            
        return img

    def _validate_config(self):
        """Validates noise and pipeline configurations."""
        if self.encoding_type not in ["qpie", "frqi"]:
            raise ValueError(f"Unsupported encoding: {self.encoding_type}")
            
        if self.algorithm_type not in ["qhed", "inversion", "brightness", "blur", "dilation", "none"]:
            raise ValueError(f"Unsupported algorithm: {self.algorithm_type}")
            
        if self.noise_config:
            for k, v in self.noise_config.items():
                if k.startswith('p_') and not (0 <= v <= 1):
                    raise ValueError(f"Noise probability {k}={v} must be between 0 and 1")

    def run(self, image_path: str, shots: int = 8192, ablation: list = None, algo_params: dict = None) -> dict:
        """
        Executes the quantum image processing experiment.
        
        Args:
            image_path (str): Path to the input image or None for synthetic patterns.
            shots (int): Number of measurement shots.
            ablation (list): List of effects to disable (e.g., ["noise", "entanglement"]).
            algo_params (dict): Parameters for the specific algorithm.
            
        Returns:
            dict: Results including reconstructed images, circuit metrics (CNOT, depth), and SSIM.
        """
        # 1. Load, Validate and Preprocess
        self._validate_config()
        img = load_and_preprocess(image_path, auto_pad=True)
        img = self._validate_image(img)
        
        vec = img.flatten()
        n_qubits = int(np.log2(len(vec)))
        
        # 2. Encoding
        if self.encoding_type == "qpie":
            qc = encode_qpie(vec)
        else:
            qc = encode_frqi(vec)
            
        # 3. Algorithm Selection
        params = algo_params or {}
        if self.algorithm_type == "qhed":
            use_entanglement = True if ablation is None or "entanglement" not in ablation else False
            final_qc = create_qhed_circuit(qc, use_entanglement=use_entanglement)
        elif self.algorithm_type == "inversion":
            final_qc = create_inversion_circuit(qc, encoding=self.encoding_type)
        elif self.algorithm_type == "brightness":
            final_qc = create_brightness_circuit(qc, encoding=self.encoding_type, **params)
        elif self.algorithm_type == "blur":
            final_qc = create_blur_circuit(qc, encoding=self.encoding_type)
        elif self.algorithm_type == "dilation":
            final_qc = create_dilation_circuit(qc, encoding=self.encoding_type)
        else:
            final_qc = qc 
            
        # Record Logical Metrics
        logical_depth = final_qc.depth()
        logical_ops = final_qc.count_ops()

        final_qc.measure_all()
        
        # 4. Simulation & Transpilation
        t_qc = transpile(final_qc, self.sim, optimization_level=1)
        
        # Decompose to basis gates for realistic CNOT count
        decomposed_qc = t_qc.decompose()
        cnot_count = decomposed_qc.count_ops().get('cx', 0)
        
        noise_model = None
        if ablation is None or "noise" not in ablation:
            noise_model = create_advanced_noise_model(**self.noise_config)
            
        backend = AerSimulator(noise_model=noise_model) if noise_model else self.sim
        result = backend.run(t_qc, shots=shots).result()
        counts = result.get_counts()
        
        # 5. Reconstruction & Advanced Metrics
        # The number of image qubits is always log2 of pixels
        image_n = int(np.log2(img.size))
        
        if self.algorithm_type == "qhed":
            recon_mode = "qhed"
        elif self.encoding_type == "frqi":
            recon_mode = "frqi"
        else:
            recon_mode = "raw"
            
        # RAW vector for scientific metrics
        processed_vec_raw = reconstruct_from_counts(counts, image_n, mode=recon_mode)
        
        # Normalized image for visualization
        processed_image_display = normalize_for_display(processed_vec_raw).reshape(img.shape)
        
        # Calculate SSIM against original
        ssim_score = calculate_ssim(img, processed_image_display)
        
        return {
            "processed_image": processed_image_display,
            "logical_depth": logical_depth,
            "transpiled_depth": t_qc.depth(),
            "gates": t_qc.size(),
            "cnot_count": cnot_count,
            "qubits": t_qc.num_qubits,
            "ssim": ssim_score,
            "raw_vec": processed_vec_raw
        }

def run_qip(image_path, noise_enabled=True, shots=8192):
    """Legacy wrapper using the new QIPPipeline class."""
    noise_config = {"p_gate": 0.01, "p_meas": 0.02} if noise_enabled else None
    pipeline = QIPPipeline(noise_config=noise_config)
    results = pipeline.run(image_path, shots=shots)
    
    # Adapt keys for backward compatibility
    original = load_and_preprocess(image_path)
    return {
        "original": original,
        "classical_baseline": classical_baseline_sobel(original),
        "quantum_clean": results["processed_image"],
        "quantum_noisy": results["processed_image"] if noise_enabled else None,
        "similarity_score": 0.0, # To be calculated if needed
        "circuit_depth": results["transpiled_depth"],
        "qubits_used": results["qubits"]
    }
