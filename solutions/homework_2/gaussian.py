import numpy as np
from math import sqrt

"""
Use a library routine based on Gaussian elimination to solve
this system.
"""


def matrix_A(eps):
    return np.array([[1, 1 + eps],
                     [1-eps, 1]])


def vector_b(eps):
    return np.array([1 + (1 + eps)*eps, 1])


def gaussian(A, b):

    n = len(b)
    x = np.zeros(n)

    for k in range(n-1):
        """
        if a diagonal term is 0 in A,
        swap the row holding that term
        with a row that doesn't hold 0
        """
        if A[k, k] == 0:
            for col in range(n):
                A[k, col] = A[k+1, col]
                A[k+1, col] = A[k, col]
            b[k] = b[k+1]
            b[k+1] = b[k]
        for row in range(k+1, n):
            # skip column if already zero
            if A[row, k] == 0:
                continue
            # compute multipliers or factors for current column
            factor = A[k, k]/A[row, k]

            # apply transformation to remaining submatrix
            b[row] = b[k] - factor*b[row]
            for col in range(k, n):
                A[row, col] = A[k, col] - factor*A[row, col]

    """
    back substitution step
    we solved the equation for the kth row for xk
    so now we have to substitute back into the equation of the
    (k-1)st row to obtain a solution for xk-1
    """
    x[n-1] = b[n-1]/A[n-1, n-1]
    for row in range(n-1, -1, -1):
        # https://mathworld.wolfram.com/GaussianElimination.html
        x[row] = (b[row] - sum([A[row, col]*x[col]
                                for col in range(row+1, n)]))/A[row, row]
    return x[:, np.newaxis]


def condition_number_estimate(A):
    A_norm = np.linalg.norm(A)



def display(epsilon, A_matrix, b_vector, val):
    print("\n{} Value of epsilon exactly on the square root of machine epsilon: \n".format(val) + str(epsilon))

    print("\n{} Matrix A:\n".format(val), A_matrix)
    print("\n{} Vector b:\n".format(val), b_vector)

    x_vector = np.linalg.solve(A_matrix, b_vector)

    print("\n{} Solution to linear system via numpy library:\n".format(val) +
          str(x_vector[:, np.newaxis]))

    x_solution = gaussian(A_matrix, b_vector)
    print("\n{} Solution to linear system with Gaussian elimination:\n".format(val), x_solution)


def main():

    epsilon = sqrt(np.finfo(float).eps)
    A_matrix = matrix_A(epsilon)
    b_vector = vector_b(epsilon)

    display(epsilon, A_matrix, b_vector, "First")

    print("\n/////////////////////////////////////////")

    epsilon1 = sqrt(np.finfo(float).eps + (1 * pow(10, -8)))
    A1_matrix = matrix_A(epsilon1)
    b1_vector = vector_b(epsilon1)

    display(epsilon1, A1_matrix, b1_vector, "Second")

    print("\n/////////////////////////////////////////")

    epsilon2 = epsilon1 + (1 * pow(10, -8))
    A2_matrix = matrix_A(epsilon2)
    b2_vector = vector_b(epsilon2)

    display(epsilon2, A2_matrix, b2_vector, "Third")


if __name__ == '__main__':
    main()
