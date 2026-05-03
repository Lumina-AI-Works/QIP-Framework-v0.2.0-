from qiskit import QuantumCircuit
import numpy as np

def _get_gray_code_sequence(n):
    """Generates a Gray Code sequence for n bits."""
    for i in range(2**n):
        yield i ^ (i >> 1)

def encode_frqi(pixel_vals):
    """
    Flexible Representation of Quantum Images (FRQI).
    Optimized with Gray Code sequencing to minimize X-gate overhead.
    """
    num_pixels = len(pixel_vals)
    n = int(np.ceil(np.log2(num_pixels)))
    qc = QuantumCircuit(n + 1)
    
    # 1. Preparation
    for i in range(n):
        qc.h(i)
        
    # 2. Optimized Gray Code State Preparation
    current_state = 0
    # Create gray code mapping to pixel values
    # Gray code ensures only 1 bit flips between pixel encodings
    gray_sequence = list(_get_gray_code_sequence(n))
    
    # We need to map gray codes back to the original pixel indices
    # or just use the gray code sequence to visit pixels in a specific order
    for i, gray_idx in enumerate(gray_sequence):
        if i >= num_pixels: break
        
        # 2a. Flip bits to match gray_idx
        # XOR of current and target tells us which bit to flip
        flip_mask = current_state ^ gray_idx
        for j in range(n):
            if (flip_mask >> j) & 1:
                qc.x(j)
        
        # 2b. Apply Rotation (Theta calculation)
        # Using the pixel value at the index represented by gray_idx? 
        # Actually, standard FRQI maps pixel i to state i. 
        # If we visit in Gray Code order, we use pixel_vals[gray_idx].
        theta = pixel_vals[gray_idx] * (np.pi / 2)
        if theta != 0:
            qc.mcry(2 * theta, list(range(n)), n)
            
        current_state = gray_idx
        
    # 3. Final cleanup (optional, but good for circuit reuse)
    for j in range(n):
        if (current_state >> j) & 1:
            qc.x(j)
            
    return qc

def encode_qpie(pixel_vals):
    """Quantum Probability Image Encoding (QPIE)"""
    num_pixels = len(pixel_vals)
    n = int(np.ceil(np.log2(num_pixels)))
    norm = np.linalg.norm(pixel_vals)
    state = pixel_vals / norm if norm > 0 else np.zeros(2**n)
    if len(state) < 2**n:
        state = np.pad(state, (0, 2**n - len(state)))
    qc = QuantumCircuit(n)
    qc.initialize(state, range(n))
    return qc
