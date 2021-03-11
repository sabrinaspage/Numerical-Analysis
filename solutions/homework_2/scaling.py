import scipy
import numpy as np
import random


"""
Using a linear system with randomly chosen matrix A,
and right-hand-side vector b chosen so that the
solution is known...
"""

A = np.array([[50, 2, 1],
              [2, 24, 6],
              [4, 7, 10]])

b = np.array([1, 1, 1])

print("Matrix A and vector b:", A, b, sep="\n")

x = np.linalg.solve(A, b)
x = x[:, np.newaxis]

print("\nSolution to matrix A:\n", x)

"""
Experiment with various scaling matrices D to see what
effect they have on the condition number of the matrix
D*A
"""

A_cond = np.linalg.cond(A)
print("\nCondition number of A alone:\n", A_cond)

# recall, the matrix is said to be ill-conditioned with
# a high condition number. a matrix is said to be well-conditioned
# with a low condition number.
# according to https://en.wikipedia.org/wiki/Condition_number, this means:
# for a small change in the inputs (independent variable/RHS of an equation)
# there is a large change in the answer or dependent variable
# the higher the condition number, the closer the matrix is to being singular
# the lower the condition number, the closer the matrix is to being nonsingular


def rand_matrix():
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 1.0)
    rand = np.array([[x, 0, 0],
                     [0, y, 0],
                     [0, 0, 1]])
    return rand


D1 = rand_matrix()
D2 = rand_matrix()
D3 = rand_matrix()

print("\nrandomly scaled D matrices", D1, D2, D3, sep="\n")

D1_A = np.matmul(D1, A)
D2_A = np.matmul(D2, A)
D3_A = np.matmul(D3, A)

print("\nvarious scaled D matrices * original matrix A",
      D1_A, D2_A, D3_A, sep="\n")

D1_A_cond = np.linalg.cond(D1_A)
D2_A_cond = np.linalg.cond(D2_A)
D3_A_cond = np.linalg.cond(D3_A)

print("\ncondition number of D matrices * matrix A",
      D1_A_cond, D2_A_cond, D3_A_cond, sep="\n")

"""
Check for the library routine for solving the linear
system DAx = Db
"""


def solve_dax_db(D_A, D, b):
    D_b = np.matmul(D, b)
    D_x = np.linalg.solve(D_A, D_b)
    return D_x[:, np.newaxis]


D1_x = solve_dax_db(D1_A, D1, b)
D2_x = solve_dax_db(D2_A, D2, b)
D3_x = solve_dax_db(D3_A, D3, b)

print("\nSolutions to D matrices * matrix A", D1_x, D2_x, D3_x, sep="\n")

# According to 2.8, in theory the solutions are not
# supposed to change, which appears to be the case above.
# However, the condition numbers seem to change drastically for
# every run of the program

"""
Compare both the relative residuals and error given by the
various scalings
"""


def residual(D_A, D_x, D, b):
    DAx = np.matmul(D_A, D_x)
    Db = np.matmul(D, b)
    D_residual = DAx - Db
    return D_residual


D1_residual = residual(D1_A, D1_x, D1, b)
D2_residual = residual(D2_A, D2_x, D2, b)
D3_residual = residual(D3_A, D3_x, D3, b)

print("\nResiduals for scaled matrices", D1_residual,
      D2_residual, D3_residual, sep="\n")

D1_residual_norm = np.linalg.norm(D1_residual)
D2_residual_norm = np.linalg.norm(D2_residual)
D3_residual_norm = np.linalg.norm(D3_residual)

print("\nResidual norms for scaled matrices", D1_residual_norm,
      D2_residual_norm, D3_residual_norm, sep="\n")

# according to page 61, a small relative residual implies a small
# relative error in the solution when, and only when, A is well
# condition. since our A is ill conditioned, as per the condition
# number being high, the residual itself is high.
# also, a small residual does not imply a small error in the solution

def relative_residual(residual_norm, approx_x):
    A_norm = np.linalg.norm(A)
    x_norm = np.linalg.norm(approx_x)
    return residual_norm/(A_norm*x_norm)

D1_rel_residual = relative_residual(D1_residual_norm, x)
D2_rel_residual = relative_residual(D2_residual_norm, x)
D3_rel_residual = relative_residual(D3_residual_norm, x)

print("\nRelative residual for scaled matrices", D1_rel_residual,
      D2_rel_residual, D3_rel_residual, sep="\n")

# accuracy is usually enhanced if all the entries of the matrix
# have about the same order of magnitude - or if the uncertainties
# in the matrix entries are all about the same size (page 82).

# if we made A to be [[1 0], [0 e]] and b to be [1 e], then we
# would have a suffiently ill conditioned linear system, because
# the condition number would be 1/e and would be very ill
# conditioned if e was small. it would then be ill-conditioned
# however, if the second row was multiplied by 1/e,
# then the matrix would be very well-conditioned, and actually
# very accurate.

# however, on page 75, it states that a small relative residual
# does not necessarily indicate that a computed solution is
# accurate unless the system is well conditioned. furthermore,
# page 61 tells us that a small relative residual implies a small
# relative error only when A is well conditioned.

# it seems that the residual is moreso determined by the
# conditioning of a matrix rather than the accuracy.