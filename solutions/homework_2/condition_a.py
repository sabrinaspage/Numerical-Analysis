import numpy as np
from scipy.linalg import lu
import random
import operations

# Condition function is built with the methods below


def generate_c():
    return np.array([random.choice([1, -1]),
                     random.choice([1, -1]),
                     random.choice([1, -1])])


def main():
    vector_c = generate_c()

    # A1 Matrix

    A1 = np.array([[10, -7, 0],
                   [-3, 2, 6],
                   [5, -1, 5]])

    p1, l1, u1 = lu(A1)

    print("\nPermutation matrix, lower triangle with unit diagonal \
diagonal elements, and U upper triangle for A1 using Scipy \n")
    print(p1, l1, u1, sep="\n")

    print("\nA1 norm \n")
    A1_norm = np.linalg.norm(A1)
    print(A1_norm)

    print("\nSolution to A1 backward substitution \n")
    A1_backward_v = operations.backward(np.transpose(u1), vector_c)
    print(A1_backward_v)

    print("\nSolution to A1 forward substitution \n")
    A1_forward_y = operations.forward(np.transpose(l1), vector_c)
    print(A1_forward_y)

    print("\nSolutions for z vector ")
    A1_z_vector = np.linalg.solve(A1, A1_forward_y)
    print(A1_z_vector)

    print("\nA1 Inverse")
    A1_norm_of_y = np.linalg.norm(A1_forward_y)
    A1_norm_of_z = np.linalg.norm(A1_z_vector)
    A1_inverse_norm = A1_norm_of_y/A1_norm_of_z
    print(A1_inverse_norm)

    print("\nA1 Estimate Condition number")
    A1_cond_num = A1_norm * A1_inverse_norm
    print(A1_cond_num)

    # A2 Matrix

    A2 = np.array([[-73, 78, 24],
                   [92, 66, 25],
                   [-80, 37, 10]])

    p2, l2, u2 = lu(A2)

    print("\n/////////////////////////////////////////////////////////////////////")

    print("\nPermutation matrix, lower triangle with unit diagonal \
diagonal elements, and U upper triangle for A2 using Scipy \n")
    print(p2, l2, u2, sep="\n")

    print("\nA2 norm \n")
    A2_norm = np.linalg.norm(A2)
    print(A1_norm)

    print("\nSolution to A2 backward substitution \n")
    A2_backward_v = operations.backward(np.transpose(u2), vector_c)
    print(A2_backward_v)

    print("\nSolution to A2 forward substitution \n")
    A2_forward_y = operations.forward(np.transpose(l2), vector_c)
    print(A2_forward_y)

    print("\nSolutions for z vector ")
    A2_z_vector = np.linalg.solve(A2, A2_forward_y)
    print(A1_z_vector)

    print("\nA2 Inverse")
    A2_norm_of_y = np.linalg.norm(A2_forward_y)
    A2_norm_of_z = np.linalg.norm(A2_z_vector)
    A2_inverse_norm = A2_norm_of_y/A2_norm_of_z
    print(A2_inverse_norm)

    print("\nA2 Estimate Condition number")
    A2_cond_num = A2_norm * A2_inverse_norm
    print(A2_cond_num)

    print("\n//////////////////////////////////////////////////////////////")

    # The condition number of the first matrix is closer to singularity
    # The condition number of the second matrix is closer to 1

    print("\nA1 Actual Condition number")
    real_cond_A1 = np.linalg.cond(A1)
    print(real_cond_A1)

    print("\nA2 Actual Condition number")
    real_cond_A2 = np.linalg.cond(A2)
    print(real_cond_A2)

    # It seems as though my estimates were far from the real answer.
    # The condition number for A1 is closer to 1, while matrix 2 is
    # far from being nonsingular.


if __name__ == '__main__':
    main()
