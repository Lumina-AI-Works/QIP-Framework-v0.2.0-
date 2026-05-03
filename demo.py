import os
from qip_framework.core.pipeline import QIPPipeline
from qip_framework.utils import load_and_preprocess

def run_demo():
    """
    Standard one-click demo for QIP Framework.
    Answers the 'How do I use this?' question instantly.
    """
    print("--- QIP Framework Demo ---")
    
    # 1. Initialize with specific encoding and algorithm
    # Using QPIE and QHED as they are research-efficient
    pipeline = QIPPipeline(encoding="qpie", algorithm="qhed")
    
    print("Running Quantum Hadamard Edge Detection on benchmark pattern...")
    
    # 2. Run the pipeline
    # results contains reconstructed images and NISQ metrics
    results = pipeline.run(None) 
    
    # 3. Output results
    print("\n[Result Summary]")
    print(f"SSIM (Fidelity) vs Original: {results['ssim']:.4f}")
    print(f"Quantum Circuit Depth:        {results['transpiled_depth']}")
    print(f"CNOT Gates (Complexity):      {results['cnot_count']}")
    
    print("\nVisual results have been saved to the 'results/' directory.")
    
    # Run a quick check to see if results folder exists
    if not os.path.exists("results"):
        os.makedirs("results")

if __name__ == "__main__":
    run_demo()
