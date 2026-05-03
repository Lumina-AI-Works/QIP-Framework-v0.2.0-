# Hardware-Aware Simulation: Noise Models

A unique feature of this framework is its integrated **NISQ (Noisy Intermediate-Scale Quantum)** simulation environment. Real-world quantum processors are susceptible to various types of noise that degrade image fidelity.

## Supported Error Types

### 1. Thermal Relaxation ($T_1$ and $T_2$)
This models the decoherence of qubits over time. 
- **$T_1$ (Longitudinal relaxation)**: The time it takes for a qubit to decay from $|1\rangle$ to $|0\rangle$.
- **$T_2$ (Transverse relaxation)**: The time it takes for a qubit to lose its phase information.

In the framework, these are configured via `t1` and `t2` parameters in `noise.py`.

### 2. Depolarizing Errors (Gate Noise)
This models the probability that a logic gate operation (like a CNOT or Hadamard) results in a completely random state. 
- Single-qubit gate errors ($p_1$)
- Two-qubit gate errors ($p_2$), typically modeled as $5 \times p_1$.

### 3. Readout Errors (Measurement Noise)
Models the probability that a $|0\rangle$ is measured as a $|1\rangle$, or vice versa. This is critical for image reconstruction as it introduces "salt and pepper" noise into the results.

---

## Configuration
You can customize the noise profile when initializing the pipeline:

```python
noise_config = {
    "p_gate": 0.01,
    "p_meas": 0.05,
    "t1": 50e-6,  # 50 microseconds
    "t2": 70e-6   # 70 microseconds
}

pipeline = QIPPipeline(noise_config=noise_config)
```

The framework also provides convenience functions for standard hardware profiles:
- `get_standard_nisq_noise()`
- `get_low_noise_model()`
