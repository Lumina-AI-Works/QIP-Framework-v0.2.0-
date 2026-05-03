# Contributing to QIP Framework

Thank you for your interest in contributing to the QIP Framework! This project aims to bridge the gap between classical image processing and quantum computing research.

## 🧪 Development Workflow

1. **Fork the Repository**: Create your own branch for features or bug fixes.
2. **Environment Setup**:
   ```bash
   pip install -r requirements.txt
   pip install pytest
   ```
3. **Coding Standards**:
   - Follow PEP 8 guidelines.
   - Use descriptive names for quantum registers and qubits.
   - Document all new algorithms with their theoretical complexity.

## 🛠️ Adding New Algorithms

To add a new quantum image algorithm:
1. Create a new function in `qip_framework/algorithms.py`.
2. Ensure it accepts a `QuantumCircuit` (encoded state) as input.
3. Add a corresponding case in `QIPPipeline.run()` in `pipeline.py`.
4. Add a test case in `tests/test_algorithms.py`.

## 📈 Benchmarking

If you are contributing research results:
- Use the `QIPPipeline` with a consistent `seed` for reproducibility.
- Compare results against at least one classical baseline (e.g., Sobel, Canny, or Gaussian Blur).
- Document the noise model used (Thermal Relaxation T1/T2 is preferred for NISQ studies).

## 📜 Code of Conduct

Please be respectful and professional in all interactions. We follow the standard Contributor Covenant.
