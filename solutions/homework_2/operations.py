import numpy as np
import random
from scipy.linalg.decomp_lu import lu

# https://algowiki-project.org/en/Forward_substitution
# page 64-65
def forward(L, v):
    (m, n) = L.shape # get the num of curresponding elements in L
    y = np.zeros(m) # create a y vector in the 3x1 shape of L
    for k in range(m):
        dot = np.dot(L[k, :k], v[:k])
        y[k] = v[k] - dot
        # update right-hand side using dot-product procedure
    return y[:, np.newaxis]

# page 64-65
def backward(U, c):
    (m, n) = U.shape # get the num of corresponding elements in L
    l = m - 1 # start at the end rather than beginning of vector
    v = np.zeros(m) # create a v vector in the 3x1 shape of L
    for k in range(m):
        dot = np.dot(U[l-k, l-k:], v[l-k:])
        v[l-k] = (1.0 / U[l-k, l-k]) * (c[l-k] - dot)
        # update right-hand side using dot-product procedure
    return v[:, np.newaxis]

def rand_matrix():
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 1.0)
    rand = np.array([[x, 0, 0],
                     [0, y, 0],
                     [0, 0, 1]])
    return rand


def solve_dax_db(D_A, D, b):
    D_b = np.matmul(D, b)
    D_x = np.linalg.solve(D_A, D_b)
    return D_x[:, np.newaxis]


def residual(D_A, D_x, D, b):
    DAx = np.matmul(D_A, D_x)
    Db = np.matmul(D, b)
    D_residual = DAx - Db
    return D_residual


def relative_residual(A, residual_norm, approx_x):
    A_norm = np.linalg.norm(A)
    x_norm = np.linalg.norm(approx_x)
    return residual_norm/(A_norm*x_norm)

def matrix_A(eps):
    return np.array([[1, 1 + eps],
                     [1-eps, 1]]).astype(np.float64)


def vector_b(eps):
    return np.array([1 + (1 + eps)*eps, 1]).astype(np.float64)


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
    return x[:, np.newaxis].astype(np.float64)


def estimate_condition_num(A, b):
    A_norm = np.linalg.norm(A)
    p1, l1, u1 = lu(A)

    A_backward_v = backward(np.transpose(u1), b)
    A_forward_y = forward(np.transpose(l1), b)
    A_z_vector = np.linalg.solve(A, A_forward_y)

    A_norm_of_y = np.linalg.norm(A_forward_y)
    A_norm_of_z = np.linalg.norm(A_z_vector)
    A_inverse_norm = A_norm_of_y/A_norm_of_z

    A_cond_num = A_norm * A_inverse_norm
    return A_cond_num


def relative_error(true_x, approx_x):
    errors = []
    for ind1, i in enumerate(true_x):
        for ind2, j in enumerate(approx_x):
            if ind1 == ind2:
                dividend = np.linalg.norm(i - j)
                divisor = np.linalg.norm(j)
                errors.append(dividend/divisor)
    return errors


def display(true_x, epsilon, A_matrix, b_vector, val):
    print("\n{} Value of epsilon exactly on the square root of machine epsilon: \n".format(
        val) + str(epsilon))

    print("\n{} Matrix A:\n".format(val), A_matrix)
    print("\n{} Vector b:\n".format(val), b_vector)

    x_vector = np.linalg.solve(A_matrix, b_vector)

    print("\n{} Solution to linear system via numpy library:\n".format(val) +
          str(x_vector[:, np.newaxis]))

    x_solution = gaussian(A_matrix, b_vector)
    print("\n{} Solution to linear system with Gaussian elimination:\n".format(
        val), x_solution)

    est_cond = estimate_condition_num(A_matrix, b_vector)
    print("\nCondition number of the {} matrix:\n".format(val), str(est_cond))

    relative_err = relative_error(true_x, x_vector)
    print("\nThe relative errors of the true value of x and the obtained value of x \
for every component in x:\n", relative_err)