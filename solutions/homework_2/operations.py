import numpy as np
import random

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