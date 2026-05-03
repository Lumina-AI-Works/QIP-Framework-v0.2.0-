import numpy as np
from qip_framework.pipeline import QIPPipeline

def test_blur_algorithm():
    """Verify the Blur algorithm runs and produces a valid output."""
    print("Testing Blur algorithm...")
    pipeline = QIPPipeline(encoding="frqi", algorithm="blur")
    # Small 4x4 image for speed
    results = pipeline.run(None, shots=1024)
    assert results['processed_image'].shape == (8, 8)
    print("[PASS] Blur algorithm executed successfully")

def test_dilation_algorithm():
    """Verify the Dilation algorithm runs and produces a valid output."""
    print("Testing Dilation algorithm...")
    pipeline = QIPPipeline(encoding="frqi", algorithm="dilation")
    results = pipeline.run(None, shots=1024)
    assert results['processed_image'].shape == (8, 8)
    print("[PASS] Dilation algorithm executed successfully")

if __name__ == "__main__":
    try:
        test_blur_algorithm()
        test_dilation_algorithm()
        print("\nAll new algorithms verified successfully!")
    except Exception as e:
        print(f"[FAIL] Algorithm verification failed: {e}")
        import traceback
        traceback.print_exc()
