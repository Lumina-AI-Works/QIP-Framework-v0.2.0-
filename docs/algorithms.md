# Algorithms Overview

The **QIP Framework** implements several core quantum algorithms for image transformation and feature extraction.

## 1. Quantum Hadamard Edge Detection (QHED)
The flagship algorithm of the framework. It extracts vertical and horizontal gradients by using:
- **Auxiliary Qubit Interference**: A Hadamard gate on an auxiliary qubit creates a superposition of the original and shifted image.
- **Cycle Shift**: A controlled incrementer shifts pixel values by 1.
- **Interference Reconstruction**: A final Hadamard gate extracts the difference between adjacent pixels.

## 2. Quantum Average Blur (Low-Pass)
This algorithm smooths images by averaging adjacent pixel values.
- **Principle**: Similar to QHED, but instead of extracting the difference, it reconstructs the sum (superposition) of adjacent pixels.
- **Effect**: Reduces high-frequency noise but softens edges.

## 3. Quantum Morphological Operations
Currently supports **Dilation**.
- **Dilation**: Mimics the classical "MAX" filter. It expands bright regions of the image. 
- **Implementation**: In this framework, dilation is approximated for FRQI using a non-linear contrast enhancement rotation that boosts higher intensity angles.

## 4. Intensity Transforms
- **Brightness Adjustment**: Rotates the color qubit (in FRQI) by a factor of $\pi$, effectively shifting the global intensity.
- **Image Inversion**: Flips the color qubit ($X$ gate), mapping white to black and vice versa.
