import numpy as np

def proj(x, y):
    return np.inner(x, y) / np.inner(x, x) * x

def gram_schmidt(V):
    U = []
    for v in V:
        q = v
        for u in U:
            q -= proj(u, q)
        U.append(q / np.linalg.norm(q))
    return np.array(U)

A = np.array([
    [-1, 1, -1, 1],
    [-1, 3, -1, 3],
    [1, 3, 5, 7]
], dtype=float)

print(gram_schmidt(A))
