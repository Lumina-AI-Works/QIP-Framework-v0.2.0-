import os
import matplotlib.pyplot as plt
from qip_framework.pipeline import QIPPipeline
from qip_framework.utils import load_and_preprocess, get_classical_baselines

def run_framework_benchmark():
    """
    Runs a full benchmark and saves visual results to the results/ directory.
    This demonstrates the framework's capability to generate scientific proof-of-results.
    """
    print("Running QIP Framework Benchmark...")
    
    # 1. Create results directory if it doesn't exist
    os.makedirs("results", exist_ok=True)
    
    # 2. Initialize pipeline
    pipeline = QIPPipeline(encoding="qpie", algorithm="qhed")
    
    # 3. Run on a complex pattern
    image_path = None # Generates a benchmark pattern
    results = pipeline.run(image_path)
    
    # 4. Get original and classical for plotting
    original = load_and_preprocess(image_path)
    classical = get_classical_baselines(original)["sobel"]
    quantum = results["processed_image"]
    
    # 5. Plotting
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    axes[0].imshow(original, cmap='gray')
    axes[0].set_title("Original Image")
    axes[0].axis('off')
    
    axes[1].imshow(classical, cmap='gray')
    axes[1].set_title("Classical Sobel")
    axes[1].axis('off')
    
    axes[2].imshow(quantum, cmap='gray')
    axes[2].set_title(f"Quantum QHED (SSIM: {results['ssim']:.3f})")
    axes[2].axis('off')
    
    plt.tight_layout()
    save_path = "results/comparison_results.png"
    plt.savefig(save_path)
    print(f"Benchmark complete. Results saved to: {save_path}")

if __name__ == "__main__":
    run_framework_benchmark()
