import os
import sys
import numpy as np
import matplotlib.pyplot as plt

# Ensure the package is importable
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from qip_framework.pipeline import QIPPipeline
from qip_framework.utils import plot_research_results

def main():
    print("--- QIP Framework: Brightness Adjustment Demo ---")
    
    # Initialize pipeline for Brightness using FRQI
    pipeline = QIPPipeline(encoding="frqi", algorithm="brightness")
    
    # Run with different brightness factors
    # factor=0.5 -> significant rotation on color qubit
    results_bright = pipeline.run("data/test.png", algo_params={"factor": 0.5})
    
    # Run clean (factor=0)
    results_clean = pipeline.run("data/test.png", algo_params={"factor": 0.0})
    
    print("Brightness adjustment complete.")
    
    # Plotting
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(results_clean["processed_image"], cmap='gray')
    axes[0].set_title("Original (Reconstructed)")
    
    axes[1].imshow(results_bright["processed_image"], cmap='gray')
    axes[1].set_title("Brighter (Quantum RY Rotation)")
    
    for ax in axes: ax.axis('off')
    
    plt.savefig("results/brightness_results.png")
    print("Results saved to 'results/brightness_results.png'")

if __name__ == "__main__":
    main()
