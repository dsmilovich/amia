import numpy as np

A = np.array([
    [1, 2, -1, 0],
    [2, 3, 1, 6],
    [0, 1, 0, 1]
], dtype=float)

U, S, VT = np.linalg.svd(A)

print("U =\n", U)
print("\nSingular values S =\n", S)
print("\nV^T =\n", VT)

S_inv = np.zeros((VT.shape[0], U.shape[0]))

for i in range(len(S)):
    if S[i] > 1e-15:
        S_inv[i, i] = 1.0 / S[i]

Adagger = VT.T @ S_inv @ U.T
result = Adagger @ np.array([1, 2, 3])

print(result)