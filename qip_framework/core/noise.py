from qiskit_aer.noise import NoiseModel, depolarizing_error, amplitude_damping_error, ReadoutError, thermal_relaxation_error
import numpy as np

def create_advanced_noise_model(p_gate=0.01, p_meas=0.05, t1=50e-6, t2=70e-6, gate_time=50e-9):
    """
    Creates a realistic NISQ noise model.
    """
    noise_model = NoiseModel()

    # 1. Gate Errors (Depolarizing)
    error_gate1 = depolarizing_error(p_gate, 1)
    error_gate2 = depolarizing_error(p_gate * 5, 2)
    noise_model.add_all_qubit_quantum_error(error_gate1, ['u1', 'u2', 'u3', 'h', 'id'])
    noise_model.add_all_qubit_quantum_error(error_gate2, ['cx'])

    # 2. Thermal Relaxation (Decoherence)
    t2 = min(t2, 2 * t1)
    error_relax_1q = thermal_relaxation_error(t1, t2, gate_time)
    error_relax_2q = error_relax_1q.tensor(error_relax_1q)
    
    noise_model.add_all_qubit_quantum_error(error_relax_1q, ['u1', 'u2', 'u3', 'h', 'id'])
    noise_model.add_all_qubit_quantum_error(error_relax_2q, ['cx'])

    # 3. Readout Errors (Measurement)
    probabilities = [[1 - p_meas, p_meas], [p_meas, 1 - p_meas]]
    error_ro = ReadoutError(probabilities)
    noise_model.add_all_qubit_readout_error(error_ro)

    return noise_model

def get_standard_nisq_noise():
    return create_advanced_noise_model(p_gate=0.001, p_meas=0.02)

def get_low_noise_model():
    return create_advanced_noise_model(p_gate=0.0001, p_meas=0.005)
