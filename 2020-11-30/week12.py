import numpy as np
np.set_printoptions(suppress=True)

def dft_matrix(n):
    omega_n = np.exp(2j * np.pi / n)
    basis = np.array([omega_n**(-i) for i in range(n)])
    return 1 / np.sqrt(n) * np.array([basis**i for i in range(n)])

def dft(f, n):
    vector = np.array([f(i) for i in range(n)])
    return dft_matrix(n) @ vector

f = lambda x: np.cos(4 * np.pi / 5 * x + np.pi / 2)
g = lambda x: 3 * np.cos(2 * np.pi / 5 * x)
h = lambda x: 3 * np.cos(8 * np.pi / 5 * x)
# print(dft_matrix(5))
print(dft(f, 5))
print(dft(g, 5))
print(dft(h, 5))
