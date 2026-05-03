import numpy as np

def calculate_cosine_similarity(v1, v2):
    """Calculates cosine similarity between two flattened images."""
    v1, v2 = v1.flatten(), v2.flatten()
    n1, n2 = np.linalg.norm(v1), np.linalg.norm(v2)
    if n1 > 0 and n2 > 0:
        return np.dot(v1, v2) / (n1 * n2)
    return 0.0

def calculate_ssim(img1, img2):
    """
    Calculates a simplified Structural Similarity Index (SSIM) using NumPy.
    """
    C1 = (0.01 * 1.0)**2
    C2 = (0.03 * 1.0)**2

    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)

    mu1 = np.mean(img1)
    mu2 = np.mean(img2)
    
    mu1_sq = mu1**2
    mu2_sq = mu2**2
    mu1_mu2 = mu1 * mu2

    sigma1_sq = np.var(img1)
    sigma2_sq = np.var(img2)
    sigma12 = np.mean(img1 * img2) - mu1_mu2

    num = (2 * mu1_mu2 + C1) * (2 * sigma12 + C2)
    den = (mu1_sq + mu2_sq + C1) * (sigma1_sq + sigma2_sq + C2)

    return num / den

def normalize_for_display(vec):
    """Scales a vector to 0-1 range for visualization."""
    if np.max(vec) > 0:
        return vec / np.max(vec)
    return vec

def reconstruct_from_counts(counts, n_qubits, mode="raw"):
    """Reconstructs an image vector from measurement counts."""
    size = 2**n_qubits
    vec = np.zeros(size)
    total_shots = sum(counts.values())

    for state, count in counts.items():
        if mode == "qhed":
            if state[0] == '1':
                idx = int(state[1:], 2)
                if idx < size:
                    vec[idx] = count
        elif mode == "frqi":
            if state[0] == '1':
                idx = int(state[1:], 2)
                if idx < size:
                    vec[idx] = count
        else:
            idx = int(state, 2)
            if idx < size:
                vec[idx] = count

    if total_shots > 0:
        vec = vec / total_shots
        
    return vec
