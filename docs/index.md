# Welcome to QIP Framework

**QIP Framework** is a modular, research-oriented library designed for investigating Quantum Image Processing (QIP) algorithms under realistic **NISQ (Noisy Intermediate-Scale Quantum)** constraints.

Developed by **M. Sowmya Priya** and **K. Lalitha**, this framework provides a high-level API to encode classical images into quantum states, apply quantum transforms, and simulate results with hardware-aware noise models.

---

## 🎯 Project Goals
- **Hardware Realism**: Bridge the gap between theoretical QIP and noisy hardware performance.
- **Reproducibility**: Provide standardized benchmarks (SSIM, Cosine Similarity) against classical baselines.
- **Optimization**: Implement efficient state preparation (Gray Code FRQI) to reduce circuit depth.

---

## 🚀 Quick Start

### Installation
```bash
pip install qip-framework
```

### Basic Usage
```python
from qip_framework.pipeline import QIPPipeline

# Initialize a pipeline with noise simulation
pipeline = QIPPipeline(encoding="qpie", algorithm="qhed")

# Run the experiment
results = pipeline.run("data/test.png")

print(f"SSIM Score: {results['ssim']:.4f}")
```

---

## 📂 Modules
- **Encoding**: Optimized FRQI and QPIE implementations.
- **Algorithms**: QHED, Blur, Dilation, and Intensity transforms.
- **Noise**: Advanced T1/T2 and Readout error modeling.
- **Analysis**: Scientific benchmarking and visualization tools.
