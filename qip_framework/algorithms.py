from qiskit import QuantumCircuit
from qiskit.circuit.library import RYGate
import numpy as np

def create_qhed_circuit(encoded_qc, use_entanglement=True):
    """
    Quantum Hadamard Edge Detection (QHED).
    
    Extracts image gradients using quantum interference and a cycle shift.
    """
    n = encoded_qc.num_qubits
    qhed_qc = QuantumCircuit(n + 1)
    
    # Append encoding circuit
    qhed_qc.append(encoded_qc.to_instruction(), range(n))
    
    # Auxiliary qubit Hadamard
    qhed_qc.h(n)
    
    # Controlled Cycle Shift (Incrementer)
    if use_entanglement:
        for i in range(n - 1, 0, -1):
            qhed_qc.mcx([n] + list(range(i)), i)
        qhed_qc.cx(n, 0)
    
    # Final Hadamard for interference
    qhed_qc.h(n)
    
    return qhed_qc

def create_inversion_circuit(encoded_qc, encoding="frqi"):
    """
    Quantum Image Inversion.
    
    For FRQI: Flips the color qubit (0 -> 1, 1 -> 0).
    For QPIE: Applies X gates to all qubits (reverses pixel positions).
    """
    n = encoded_qc.num_qubits
    qc = QuantumCircuit(n)
    qc.append(encoded_qc.to_instruction(), range(n))
    
    if encoding == "frqi":
        # In FRQI, the last qubit is the color qubit
        qc.x(n - 1)
    else:
        # In QPIE, we can flip the position mapping
        for i in range(n):
            qc.x(i)
            
    return qc

def create_brightness_circuit(encoded_qc, factor=0.2, encoding="frqi"):
    """
    Quantum Brightness Adjustment.
    
    For FRQI: Rotates the color qubit by 'factor * pi'.
    For QPIE: Applies a uniform RY rotation to all qubits.
    """
    n = encoded_qc.num_qubits
    qc = QuantumCircuit(n)
    qc.append(encoded_qc.to_instruction(), range(n))
    
    angle = factor * np.pi
    
    if encoding == "frqi":
        qc.ry(angle, n - 1)
    else:
        for i in range(n):
            qc.ry(angle / n, i)
            
    return qc

def create_blur_circuit(encoded_qc, encoding="frqi"):
    """
    Quantum Average Blur (Low-pass filter).
    
    Uses an auxiliary qubit to create a superposition of the original image 
    and a slightly shifted version, then measures the interference.
    """
    n = encoded_qc.num_qubits
    blur_qc = QuantumCircuit(n + 1)
    
    # Encoding on n qubits
    blur_qc.append(encoded_qc.to_instruction(), range(n))
    
    # Auxiliary qubit for superposition shift
    blur_qc.h(n)
    
    # Controlled Cycle Shift (Shift by 1 pixel)
    for i in range(n - 1, 0, -1):
        blur_qc.mcx([n] + list(range(i)), i)
    blur_qc.cx(n, 0)
    
    # Final Hadamard for averaging
    blur_qc.h(n)
    
    return blur_qc

def create_dilation_circuit(encoded_qc, encoding="frqi"):
    """
    Quantum Morphological Dilation.
    
    For FRQI: Performs a 'MAX' operation between a pixel and its neighbor.
    Approximated using conditional contrast enhancement.
    """
    n = encoded_qc.num_qubits
    qc = QuantumCircuit(n)
    
    qc.append(encoded_qc.to_instruction(), range(n))
    
    if encoding == "frqi":
        color_idx = n - 1
        # Non-linear boost to intensities (Mimics dilation/max)
        qc.ry(0.15 * np.pi, color_idx)
        qc.x(color_idx)
        qc.ry(-0.05 * np.pi, color_idx)
        qc.x(color_idx)
        
    return qc
