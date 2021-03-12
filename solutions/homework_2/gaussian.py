import numpy as np
from scipy.linalg import lu
import solutions.homework_2.operations as operations
from math import sqrt

"""
Use a library routine based on Gaussian elimination to solve
this system.
"""

def main():

    epsilon = sqrt(np.finfo(float).eps)
    true_x = np.array([1, epsilon])

    print("\nNOTE: the true value of x is:\n" + str(true_x[:, np.newaxis]))

    A_matrix = operations.matrix_A(epsilon)
    b_vector = operations.vector_b(epsilon)

    operations.display(true_x, epsilon, A_matrix, b_vector, "First")

    print("\n/////////////////////////////////////////")

    epsilon1 = sqrt(np.finfo(float).eps + (1.5 * pow(10, -16)))
    A1_matrix = operations.matrix_A(epsilon1)
    b1_vector = operations.vector_b(epsilon1)

    operations.display(true_x, epsilon1, A1_matrix, b1_vector, "Second")

    print("\n/////////////////////////////////////////")

    epsilon2 = sqrt(np.finfo(float).eps + (2 * pow(10, -16)))
    A2_matrix = operations.matrix_A(epsilon2)
    b2_vector = operations.vector_b(epsilon2)

    operations.display(true_x, epsilon2, A2_matrix, b2_vector, "Third")

    print("\n\tIt seems that the relative error for the first components of x \
is extremely small (to the -08 power). The relative error for the second components \
of x is infinity, because the approximate x vector has a 0 value. \
    \n\
\tThe accuracy of each component is determined by the condition number (page 57). Luckily, \
The condition number is not greater than 10^4, so no correct digits in the solution \
were lost for x. The relative error in smaller components can be much larger (hence 0) \
because a vector norm is dominated by the largest components of a vector. \
    \n\
\tWe can argue that the matrix provided is a well-conditioned matrix with good scaling \
(page 60). It may even provide a small relative residual, which implied a relative \
error in the solution when, and only when, A is well-conditioned. (page 61)")

if __name__ == '__main__':
    main()
