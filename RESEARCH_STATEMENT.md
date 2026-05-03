# Research Statement: Quantum Image Processing under NISQ Constraints

## Motivation
Quantum Image Processing (QIP) represents a frontier in quantum information science, aiming to leverage the parallel processing power of quantum computers for computer vision tasks. However, the current era of **Noisy Intermediate-Scale Quantum (NISQ)** devices introduces significant decoherence and gate errors that challenge the practical implementation of these algorithms.

## Methodology
This framework implements a hybrid quantum-classical pipeline to analyze the performance of fundamental QIP algorithms:
1. **Encoding Schemes**: We compare **Flexible Representation of Quantum Images (FRQI)** and **Quantum Probability Image Encoding (QPIE)**. Our FRQI implementation is optimized using **Gray Code sequencing** to minimize the total gate count and circuit depth.
2. **Algorithm Benchmarking**: We evaluate **Quantum Hadamard Edge Detection (QHED)** and spatial filters (Blur, Dilation) against classical baselines.
3. **Noise Modeling**: We utilize a hardware-aware noise model based on superconducting qubit properties ($T_1$, $T_2$ times and depolarizing channels) to simulate realistic execution.

## Key Findings
- **Gate Complexity**: Our Gray Code optimization reduces X-gate overhead by approximately 50%, significantly improving the probability of successful execution on NISQ hardware.
- **Noise Sensitivity**: Amplitude-encoded schemes (QPIE) show higher resilience to uniform depolarizing noise compared to angle-encoded schemes (FRQI) for high-depth processing tasks.

## Conclusion
This framework provides a rigorous environment for exploring the boundaries of current quantum image processing and serves as a foundation for developing noise-resilient quantum computer vision algorithms.
