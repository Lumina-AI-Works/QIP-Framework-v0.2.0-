import sys
from qip_framework import QIPPipeline

def run_inference(image_path):
    """
    Simplified inference script for the QIP Framework.
    Allows for quick processing of a single image.
    """
    print(f"Running inference on {image_path}...")
    
    # Default high-fidelity settings
    pipeline = QIPPipeline(encoding="qpie", algorithm="qhed")
    
    try:
        results = pipeline.run(image_path)
        print(f"Success! Output fidelity (SSIM): {results['ssim']:.4f}")
    except Exception as e:
        print(f"Error during inference: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python inference.py <image_path>")
        sys.exit(1)
        
    run_inference(sys.argv[1])
