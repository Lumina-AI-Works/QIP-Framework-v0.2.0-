import numpy as np
from qip_framework.encoding import encode_qpie, encode_frqi
from qip_framework.algorithms import create_qhed_circuit, create_inversion_circuit

def test_qhed_structure():
    pixels = np.random.rand(16) # 4 qubits
    encoded = encode_qpie(pixels)
    qhed = create_qhed_circuit(encoded)
    # 4 encoded qubits + 1 auxiliary = 5
    assert qhed.num_qubits == 5

def test_inversion_structure():
    pixels = np.random.rand(16)
    encoded = encode_frqi(pixels) # 4 + 1 = 5 qubits
    inv = create_inversion_circuit(encoded, encoding="frqi")
    assert inv.num_qubits == 5
    # Should have at least one X gate for inversion
    assert 'x' in inv.count_ops()
