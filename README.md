# QIP Framework v0.2.0

**Hybrid Quantum–Classical Image Processing Framework for NISQ-Era Analysis**

[![PyPI version](https://img.shields.io/pypi/v/qip-framework.svg)](https://pypi.org/project/qip-framework/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🔬 Research Context
### The Problem
Quantum Image Processing (QIP) promises exponential advantages in computational complexity and storage. However, two major hurdles remain:
1. **The State Preparation Bottleneck**: Encoding classical data into quantum states (FRQI, NEQR) is often as expensive as the processing itself.
2. **NISQ Constraints**: Near-term quantum devices are noisy. Understanding how **T1/T2 relaxation** and **gate errors** impact image structural fidelity (SSIM) is critical for moving QIP from theory to practice.

### Our Solution
We present a modular framework designed to analyze these trade-offs. By implementing optimized encoding (Gray Code) and realistic hardware-aware noise models, this framework allows researchers to benchmark quantum algorithms (QHED, Blur, Dilation) against classical baselines under realistic constraints.

## 👥 Authors
- **[M. Sowmya Priya](https://github.com/Sowmyapriya-Mahamkali)**
- **[K. Lalitha](https://github.com/Lalitha-Koruprolu)**

*Equal contribution across mathematical modeling, circuit optimization, and benchmarking.*

---

## 🛠️ Framework Architecture
The project is structured into functional subpackages to reflect a professional scientific identity:

```text
qip_project/
├── qip_framework/
│   ├── core/           # Pipeline orchestration & Noise modeling
│   ├── encoding/       # State preparation (Gray-Code FRQI, QPIE)
│   ├── processing/     # Quantum circuits (QHED, Blur, Dilation)
│   ├── benchmarking/   # Scientific metrics (SSIM, Cosine Similarity)
│   └── utils.py        # I/O & Padding
├── demo.py             # One-click execution script
├── results/            # Proof-of-results (Visualizations & Data)
└── docs/               # Technical theory guides
```

## 📊 Scientific Weight & Evaluation
This framework doesn't just "process images"—it evaluates performance.
- **Structural Similarity Index (SSIM)**: Used instead of simple MSE to measure perceptual quality.
- **Ablation Studies**: Built-in support to isolate noise effects vs. algorithmic performance.
- **Hardware Metrics**: Automated reporting of CNOT counts and transpiled circuit depth.

## ▶️ Usage Clarity

### Installation
```bash
pip install qip-framework
```

### Run the Demo
The simplest way to see the framework in action is:
```bash
python demo.py
```

### High-Level API
```python
from qip_framework import QIPPipeline

# 1. Initialize with hardware-aware noise
pipeline = QIPPipeline(encoding="qpie", algorithm="qhed")

# 2. Execute research pipeline
results = pipeline.run("path/to/image.png")

# 3. Access scientific data
print(f"SSIM Score: {results['ssim']:.4f}")
```

---

Developed at **[Lumina-AI-Works](https://github.com/Lumina-AI-Works)**.
