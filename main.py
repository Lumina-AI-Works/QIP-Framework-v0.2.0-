import argparse
import os
from qip_framework import QIPPipeline

def main():
    parser = argparse.ArgumentParser(description="QIP Framework: Hybrid Quantum-Classical Image Processing")
    parser.add_argument("--image", type=str, default="data/sample.png", help="Path to input image")
    parser.add_argument("--encoding", type=str, default="qpie", choices=["qpie", "frqi"], help="Quantum encoding method")
    parser.add_argument("--algo", type=str, default="qhed", choices=["qhed", "blur", "dilation", "inversion"], help="Algorithm to run")
    parser.add_argument("--shots", type=int, default=8192, help="Number of quantum simulation shots")
    
    args = parser.parse_args()
    
    print(f"--- QIP Framework Entry Point ---")
    print(f"Algorithm: {args.algo}")
    print(f"Encoding:  {args.encoding}")
    print(f"Image:     {args.image}")
    
    # Initialize Pipeline
    pipeline = QIPPipeline(encoding=args.encoding, algorithm=args.algo)
    
    # Run
    print("\nExecuting Quantum Pipeline...")
    results = pipeline.run(args.image, shots=args.shots)
    
    # Display Results
    print("\n[Results]")
    print(f"SSIM Score:       {results['ssim']:.4f}")
    print(f"CNOT Gate Count:  {results['cnot_count']}")
    print(f"Circuit Depth:    {results['transpiled_depth']}")
    
    print("\nProcess complete. Results saved to the 'results/' folder.")

if __name__ == "__main__":
    main()
