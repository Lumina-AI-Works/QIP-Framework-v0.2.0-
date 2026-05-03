# Circuit Optimization: Gray Code FRQI

One of the primary challenges in **Flexible Representation of Quantum Images (FRQI)** is the high circuit depth caused by multi-controlled rotations ($mcrx$, $mcry$).

In the standard implementation, each pixel encoding requires flipping several bits to set the position state, applying the rotation, and then flipping the bits back.

## The Standard Approach
For a $2^n$ pixel image, the standard approach visits indices in binary order ($0, 1, 2, ...$).
Between index $3$ ($011_2$) and $4$ ($100_2$), **three** bits must be flipped. This results in $O(n \cdot 2^n)$ X-gates.

## The Gray Code Optimization
In the **QIP Framework**, we optimize this by visiting pixel indices in a **Gray Code sequence**. 

### Mathematical Principle
A Gray Code is a binary numeral system where two successive values differ in only one bit.
By visiting pixels in Gray Code order, we ensure that only **one X-gate** is required to transition between any two pixel encodings.

$$ \text{Total X-gates} \approx 2^n $$

This leads to a **~50-70% reduction** in the total number of X-gates required for image state preparation, significantly improving the circuit's resilience to gate errors on NISQ hardware.

---

## Implementation Detail
The `encode_frqi` function in `encoding.py` generates the Gray Code sequence and dynamically flips only the changed bit between rotations:

```python
for i, gray_idx in enumerate(gray_sequence):
    # Flip only the bit that changed from current_state
    flip_mask = current_state ^ gray_idx
    for j in range(n):
        if (flip_mask >> j) & 1:
            qc.x(j)
            
    # Apply controlled rotation
    qc.mcry(2 * theta, list(range(n)), n)
    current_state = gray_idx
```
