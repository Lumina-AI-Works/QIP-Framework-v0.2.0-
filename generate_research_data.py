import pandas as pd
import numpy as np
from qip_framework import QIPPipeline

def generate_scientific_dataset():
    """
    Generates a CSV dataset of algorithm performance under varying noise.
    Demonstrates the framework's capability for large-scale ablation studies.
    """
    print("Generating Scientific Benchmark Data...")
    
    noise_levels = [0.0, 0.01, 0.05, 0.1]
    encodings = ["qpie", "frqi"]
    results_list = []
    
    for enc in encodings:
        for noise in noise_levels:
            print(f"  Testing {enc} at {noise*100}% noise...")
            config = {"p_gate": noise, "p_meas": noise*2}
            pipeline = QIPPipeline(encoding=enc, algorithm="qhed", noise_config=config)
            
            # Run simulation
            res = pipeline.run(None)
            
            results_list.append({
                "encoding": enc,
                "noise_gate_prob": noise,
                "ssim": res["ssim"],
                "cnot_count": res["cnot_count"],
                "circuit_depth": res["transpiled_depth"]
            })
            
    df = pd.DataFrame(results_list)
    os.makedirs("results", exist_ok=True)
    df.to_csv("results/benchmark_data.csv", index=False)
    print("\nScientific data saved to results/benchmark_data.csv")

if __name__ == "__main__":
    import os
    generate_scientific_dataset()
