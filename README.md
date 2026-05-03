# QIP Framework v0.2.0

**Hybrid Quantum–Classical Image Processing Framework**

[![PyPI version](https://img.shields.io/pypi/v/qip-framework.svg)](https://pypi.org/project/qip-framework/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

---

## 🚀 Overview
The **QIP Framework** is a modular, research-oriented library designed for investigating Quantum Image Processing (QIP) algorithms under realistic **NISQ (Noisy Intermediate-Scale Quantum)** constraints. 

Classical image processing is computationally expensive for high-resolution data. While QIP offers potential exponential advantages in storage and processing speed, current hardware noise (decoherence, gate errors) poses a significant bottleneck. This framework provides the tools to analyze these trade-offs through hardware-aware simulation and rigorous benchmarking.

## 👥 Authors
- **[M. Sowmya Priya](https://github.com/Sowmyapriya-Mahamkali)**: Core Algorithm Design & Noise Simulation
- **[K. Lalitha](https://github.com/Lalitha-Koruprolu)**: Encoding Optimization & Benchmarking

*Equal contribution across research statement, design, implementation, and benchmarking.*

## ⚙️ Key Features
- **Flexible Encoding**: Optimized **Gray Code FRQI** (Flexible Representation of Quantum Images) and **QPIE** (Quantum Probability Image Encoding).
- **Advanced Processing**: 
    - **QHED**: Quantum Hadamard Edge Detection.
    - **Spatial Filters**: Quantum Average Blur (Low-pass) and Morphological Dilation.
    - **Intensity Transforms**: Parametric brightness adjustment and inversion.
- **Hardware-Aware Simulation**: Realistic noise models including **Thermal Relaxation (T1/T2)**, depolarizing errors, and measurement readout errors.
- **Scientific Benchmarking**: Automated comparison tools against classical baselines (Sobel, Canny) using **SSIM** and **Cosine Similarity**.

## 📂 Project Structure
The framework is organized into specialized subpackages for modular research:

```text
qip_project/
├── qip_framework/
│   ├── encoding/       # State preparation (FRQI, QPIE)
│   ├── processing/     # Quantum circuits (QHED, Blur, Dilation)
│   ├── benchmarking/   # Metrics (SSIM, Similarity)
│   ├── noise.py        # NISQ error models
│   ├── pipeline.py     # Research orchestration API
│   └── utils.py        # Image I/O and padding
├── docs/               # Technical theory and optimization guides
├── examples/           # Ready-to-run research demos
├── tests/              # Unit tests for core logic
├── results/            # Proof-of-results (Visualizations)
└── pyproject.toml      # Package metadata
```

## 🧪 Research Results
The framework enables detailed ablation studies. Below are typical outputs comparing classical baselines with clean and noisy quantum execution.

### Quantum Hadamard Edge Detection (QHED)
![QHED Comparison](results/comparison_results.png)
*Comparison between Original, Classical Sobel, and Quantum QHED.*

## ▶️ Quick Start

### Installation
```bash
pip install qip-framework
```

### Example Usage
```python
from qip_framework.pipeline import QIPPipeline

# 1. Initialize research pipeline
pipeline = QIPPipeline(encoding="qpie", algorithm="qhed")

# 2. Run experiment
results = pipeline.run("data/test.png")

# 3. Analyze scientific metrics
print(f"SSIM Score: {results['ssim']:.4f}")
print(f"CNOT Count: {results['cnot_count']}")
```

## 📌 Future Work
- **Quantum Attention Mechanisms**: Investigating attention-based image feature extraction.
- **Error Mitigation**: Integrating Zero-Noise Extrapolation (ZNE) for improved fidelity.

---

Developed at **[Lumina-AI-Works](https://github.com/Lumina-AI-Works)**. Distributed under the MIT License.
