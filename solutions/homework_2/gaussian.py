import numpy as np
from math import sqrt

epsilon = sqrt(np.finfo(float).eps)
A_matrix = np.array([[1, 1 + epsilon],
     [1-epsilon, 1]])

b_vector = np.array([1 + (1 + epsilon)*epsilon, 1])


def gaussian(A, b):
    """
    solve Ax = B using Guassian elimination and LU decomposition
    """

    n = len(b)
    x = np.zeros(n)

    for k in range(n-1):
        # swap two rows if the diagonal term is 0
        if A[k, k] == 0:
            for col in range(n):
                A[k, col] = A[k+1, col]
                A[k+1, col] = A[k, col]
            b[k] = b[k+1]
            b[k+1] = b[k]
        for row in range(k+1, n):
            if A[row, k] == 0:
                continue
            factor = A[k, k]/A[row, k]

            b[row] = b[k] - factor*b[row]
            for col in range(k, n):
                A[row, col] = A[k, col] - factor*A[row, col]

    # back substitution step
    x[n-1] = b[n-1]/A[n-1, n-1]
    for row in range(n-1, -1, -1):
        x[row] = (b[row] - sum([A[row, col]*x[col]
                                for col in range(row+1, n)]))/A[row, row]
    return x[:, np.newaxis]


print(
    gaussian(A_matrix, b_vector))
