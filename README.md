# QIP Framework v0.2.1

**Hybrid Quantum–Classical Image Processing Framework for NISQ-Era Analysis**

[![PyPI version](https://img.shields.io/pypi/v/qip-lumina.svg)](https://pypi.org/project/qip-lumina/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🔬 Research Context

### The Problem

Quantum Image Processing (QIP) promises exponential advantages in computational complexity and storage. However, current hardware noise (decoherence, gate errors) poses a significant bottleneck. This framework provides the tools to analyze these trade-offs through hardware-aware simulation and rigorous benchmarking.

### Our Solution

We present a modular framework designed to analyze these trade-offs. By implementing optimized Gray Code encoding and realistic hardware-aware noise models, this framework allows researchers to benchmark quantum algorithms against classical baselines under realistic constraints.

---

## 👥 Authors

- **[M. Sowmya Priya](https://github.com/Sowmyapriya-Mahamkali)**
- **[K. Lalitha](https://github.com/Lalitha-Koruprolu)**

---

## 🛠️ Framework Architecture

The project follows a modular research-oriented architecture.

```text
qip_project/
├── qip_framework/      # Core Library Logic
├── main.py             # System entry point (CLI)
├── inference.py        # Single-image processing script
├── scripts/            # Benchmarking & Data generation tools
├── data/               # Sample research datasets
├── results/            # Experimental outputs & CSV files
└── docs/               # Technical documentation
```

---

# ▶️ Installation

Install directly from PyPI:

```bash
pip install qip-lumina
```

---

# 🚀 Usage

## 1. Run a Complete Experiment

```bash
python main.py --algo qhed --encoding qpie --image data/sample.png
```

## 2. Single Image Processing

```bash
python inference.py path/to/image.png
```

## 3. Generate Benchmark Dataset

```bash
python scripts/generate_research_data.py
```

---

## 📦 Features

- Hybrid Quantum-Classical Image Processing
- FRQI & QPIE Image Encoding
- Quantum Edge Detection (QHED)
- Hardware-aware NISQ Noise Simulation
- Classical vs Quantum Benchmarking
- Research Dataset Generation
- Modular Research Framework
- CLI-based Experiment Pipeline

---

## 📚 Requirements

- Python 3.8+
- Qiskit
- Qiskit Aer
- OpenCV
- NumPy
- Pandas
- Matplotlib
- Scikit-image

---

## 📄 License

This project is licensed under the MIT License.

---

## 🏢 Developed At

**Lumina-AI-Works**

https://github.com/Lumina-AI-Works
