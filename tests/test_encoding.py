import numpy as np
import pytest
from qip_framework.encoding import encode_qpie, encode_frqi

def test_qpie_qubits():
    # 8x8 image = 64 pixels -> 6 qubits
    pixels = np.random.rand(64)
    qc = encode_qpie(pixels)
    assert qc.num_qubits == 6

def test_frqi_qubits():
    # 8x8 image = 64 pixels -> 6 position qubits + 1 color qubit = 7
    pixels = np.random.rand(64)
    qc = encode_frqi(pixels)
    assert qc.num_qubits == 7

def test_invalid_dimensions():
    # Framework should handle non-power-of-two by padding in encoding
    pixels = np.random.rand(10)
    qc = encode_qpie(pixels)
    # log2(10) -> next power is 16 -> 4 qubits
    assert qc.num_qubits == 4
