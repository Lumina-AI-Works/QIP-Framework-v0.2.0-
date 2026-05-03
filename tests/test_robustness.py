import numpy as np
import pytest
from qip_framework.pipeline import QIPPipeline
from qip_framework.utils import load_and_preprocess

def test_padding_support():
    """Verify that non-power-of-two images are padded correctly."""
    # Create a 6x6 image (not a power of two)
    img_6x6 = np.random.rand(6, 6)
    pipeline = QIPPipeline(encoding="qpie", algorithm="none")
    
    # We need to save it to a temporary path or mock load_and_preprocess
    # Actually, we can just test load_and_preprocess directly first
    from qip_framework.utils import pad_to_power_of_two
    padded = pad_to_power_of_two(img_6x6)
    assert padded.shape == (8, 8)
    assert np.all(padded[:6, :6] == img_6x6)
    assert np.all(padded[6:, :] == 0)
    assert np.all(padded[:, 6:] == 0)

def test_rgb_conversion():
    """Verify that RGB images are converted to grayscale."""
    # Create a dummy 8x8x3 RGB image
    img_rgb = np.random.rand(8, 8, 3)
    pipeline = QIPPipeline()
    # This should print a warning but not fail
    grayscale = pipeline._validate_image(img_rgb)
    assert len(grayscale.shape) == 2
    assert grayscale.shape == (8, 8)

def test_validation_errors():
    """Verify that invalid inputs raise appropriate errors."""
    pipeline = QIPPipeline()
    
    # Non-normalized values
    with pytest.raises(ValueError, match="normalized"):
        pipeline._validate_image(np.array([[2.0]]))
        
    # Invalid encoding
    pipeline.encoding_type = "invalid"
    with pytest.raises(ValueError, match="Unsupported encoding"):
        pipeline.run(None)

def test_gray_code_frqi():
    """Verify FRQI encoding still works and check complexity roughly."""
    from qip_framework.encoding import encode_frqi
    pixel_vals = np.array([0.1, 0.2, 0.3, 0.4])
    qc = encode_frqi(pixel_vals)
    # 2 qubits for 4 pixels + 1 color qubit = 3 qubits
    assert qc.num_qubits == 3
    # Check that we have X gates (but hopefully fewer than before)
    ops = qc.count_ops()
    print(f"Debug: ops = {ops}")
    assert 'x' in ops
    # Depending on Qiskit version, it might be 'mcry' or 'ry'
    assert 'mcry' in ops or 'ry' in ops

if __name__ == "__main__":
    # Run tests manually
    try:
        test_padding_support()
        print("[PASS] Padding test passed")
        test_rgb_conversion()
        print("[PASS] RGB conversion test passed")
        test_validation_errors()
        print("[PASS] Validation errors test passed")
        test_gray_code_frqi()
        print("[PASS] Gray Code FRQI test passed")
        print("\nAll robustness tests passed successfully!")
    except Exception as e:
        print(f"[FAIL] Test failed: {e}")
        import traceback
        traceback.print_exc()
