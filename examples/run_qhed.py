import os
import sys
import numpy as np
from qiskit import transpile
from qiskit_aer import AerSimulator

# Ensure the package is importable if not installed
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from qip_framework import (
    load_and_preprocess, 
    classical_baseline_sobel, 
    calculate_cosine_similarity,
    calculate_ssim,
    QIPPipeline,
    plot_research_results
)

def main():
    print("--- QIP Framework: Edge Detection Demo ---")
    
    # 1. Load Data
    img = load_and_preprocess("data/test.png")
    vec = img.flatten()
    n_qubits = int(np.log2(len(vec)))
    
    # 2. Classical Baseline
    print("Computing classical baseline...")
    classical_edges = classical_baseline_sobel(img)
    
    # 3. Quantum Pipeline
    print("Executing Quantum QHED...")
    pipeline = QIPPipeline(encoding="qpie", algorithm="qhed")
    
    # Run clean simulation for benchmarking
    results = pipeline.run("data/test.png", shots=8192, ablation=["noise"])
    edges_clean = results["processed_image"]
    
    # Run noisy simulation
    results_noisy = pipeline.run("data/test.png", shots=8192)
    edges_noisy = results_noisy["processed_image"]
    
    # 4. Advanced Research Results
    similarity = calculate_cosine_similarity(edges_clean, edges_noisy)
    ssim_val = calculate_ssim(edges_clean, edges_noisy)
    
    print("-" * 30)
    print(f"QUANTUM RESEARCH METRICS:")
    print(f"Circuit Depth:   {results['transpiled_depth']}")
    print(f"CNOT Count:      {results['cnot_count']}")
    print(f"Cosine Sim:      {similarity:.4f}")
    print(f"SSIM Index:      {ssim_val:.4f}")
    print("-" * 30)
    
    # 5. Visualization
    print("Saving research plots to 'results/comparison_results.png'...")
    plot_research_results(img, classical_edges, edges_clean, noisy=edges_noisy, filename="results/comparison_results.png")
    
    print("Demo complete.")

if __name__ == "__main__":
    main()
