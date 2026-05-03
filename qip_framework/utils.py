import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

def set_seed(seed=42):
    """Sets global seeds for reproducibility."""
    np.random.seed(seed)
    random.seed(seed)

def generate_checkerboard(size=(8, 8), square_size=2):
    """Generates a deterministic checkerboard pattern for benchmarking."""
    h, w = size
    img = np.zeros(size)
    for i in range(h):
        for j in range(w):
            if ((i // square_size) + (j // square_size)) % 2 == 0:
                img[i, j] = 1.0
    return img

def generate_complex_pattern(size=(8, 8)):
    """Generates a complex pattern with diagonal and block edges."""
    img = np.zeros(size)
    h, w = size
    # Diagonal line
    for i in range(min(h, w)):
        img[i, i] = 1.0
    # Central block
    img[h//4:3*h//4, w//4:3*w//4] = 0.5
    return img

def is_power_of_two(n):
    """Checks if a number is a power of two."""
    return (n & (n - 1) == 0) and n != 0

def next_power_of_two(n):
    """Calculates the next power of two for a given number."""
    return 1 if n == 0 else 2**(n - 1).bit_length()

def pad_to_power_of_two(img):
    """
    Pads a square image to the next power of two dimensions.
    Used to ensure compatibility with quantum circuits.
    """
    h, w = img.shape
    new_size = next_power_of_two(max(h, w))
    
    if h == new_size and w == new_size:
        return img
        
    padded_img = np.zeros((new_size, new_size))
    padded_img[:h, :w] = img
    return padded_img

def load_and_preprocess(path=None, size=(8, 8), pattern="checkerboard", auto_pad=True):
    """
    Loads an image from disk or generates a benchmark pattern.
    Supports automatic padding to power-of-two dimensions.
    """
    import os
    if path and os.path.exists(path):
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        # If size is provided, we resize, else we keep original and pad
        if size:
            img = cv2.resize(img, size)
        img = img / 255.0
    else:
        if pattern == "checkerboard":
            img = generate_checkerboard(size)
        elif pattern == "complex":
            img = generate_complex_pattern(size)
        else:
            img = generate_checkerboard(size)
            
    if auto_pad:
        img = pad_to_power_of_two(img)
        
    return img

def get_classical_baselines(img):
    """
    Computes multiple classical edge detection baselines for comparison.
    
    Args:
        img (numpy.ndarray): Grayscale image (0.0 to 1.0).
        
    Returns:
        dict: Dictionary containing 'sobel', 'canny', and 'thresh' results.
    """
    # 1. Sobel
    sx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobel = np.sqrt(sx**2 + sy**2)
    sobel = sobel / np.max(sobel) if np.max(sobel) > 0 else sobel

    # 2. Canny (Thresholds adjusted for normalized 0-1 image)
    img_uint8 = (img * 255).astype(np.uint8)
    canny = cv2.Canny(img_uint8, 100, 200) / 255.0

    # 3. Gaussian + Threshold
    blur = cv2.GaussianBlur(img, (3, 3), 0)
    _, thresh = cv2.threshold((blur*255).astype(np.uint8), 127, 255, cv2.THRESH_BINARY)
    thresh = thresh / 255.0

    return {"sobel": sobel, "canny": canny, "thresh": thresh}

def plot_research_results(original, classical, quantum, noisy=None, filename="research_results.png"):
    """
    Generates a professional research-grade visualization including difference heatmaps.
    
    Args:
        original (numpy.ndarray): The original input image.
        classical (numpy.ndarray): Classical baseline result.
        quantum (numpy.ndarray): Quantum (clean simulation) result.
        noisy (numpy.ndarray, optional): Quantum (noisy simulation) result.
        filename (str): Output filename for the plot.
    """
    cols = 4 if noisy is not None else 3
    fig, axes = plt.subplots(2, cols, figsize=(4*cols, 8))
    
    # Row 1: Images
    axes[0, 0].imshow(original, cmap='gray')
    axes[0, 0].set_title("Original")
    
    axes[0, 1].imshow(classical, cmap='gray')
    axes[0, 1].set_title("Classical (Sobel)")
    
    axes[0, 2].imshow(quantum, cmap='gray')
    axes[0, 2].set_title("Quantum (Clean)")
    
    if noisy is not None:
        axes[0, 3].imshow(noisy, cmap='gray')
        axes[0, 3].set_title("Quantum (Noisy)")

    # Row 2: Heatmaps / Differences
    # Difference between classical and quantum clean
    diff = np.abs(classical - quantum)
    im = axes[1, 1].imshow(diff, cmap='hot')
    axes[1, 1].set_title("Diff: Class vs Q-Clean")
    plt.colorbar(im, ax=axes[1, 1])

    if noisy is not None:
        diff_noise = np.abs(quantum - noisy)
        im2 = axes[1, 3].imshow(diff_noise, cmap='hot')
        axes[1, 3].set_title("Diff: Clean vs Noisy")
        plt.colorbar(im2, ax=axes[1, 3])

    # Hide unused axes in row 2
    axes[1, 0].axis('off')
    if noisy is None:
        # If no noisy, 3 cols, hide 1st and 3rd in second row? 
        # Actually axes is 2x3 or 2x4.
        # Let's just hide everything that wasn't explicitly used above.
        pass

    for ax in axes.flatten():
        # Check if it has an image or a title set, if not, hide axis
        if not ax.get_images() and not ax.get_title():
            ax.axis('off')
        
    plt.tight_layout()
    plt.savefig(filename)
    print(f"Research results saved to {filename}")

def classical_baseline_sobel(img):
    """
    Legacy alias for backward compatibility.
    """
    return get_classical_baselines(img)["sobel"]

def plot_comparison(original, classical, quantum, filename="results.png"):
    """
    Legacy alias for backward compatibility.
    """
    return plot_research_results(original, classical, quantum, filename=filename)

