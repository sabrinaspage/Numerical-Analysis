from scipy.optimize import fsolve
from mpmath.math2 import cbrt

def func(p):
    x1, x2, w1, w2 = p

    eq1 = w1 + w2 - 2
    eq2 = (w1 * x1) + (w2 * x2) - 0
    eq3 = (w1 * x1**2) + (w2 * x2**2) - 2/3
    eq4 = (w1 * x1**3) + (w2 * x2**3) - 0

    return (eq1, eq2, eq3, eq4)

x1, x2, w1, w2 = fsolve(func, (-1, 1, 1/cbrt(3), 1/cbrt(3)))

print(x1, x2, w1, w2, sep='\n')

# According to Gauss-Legendre quadrature
# https://en.wikipedia.org/wiki/Gaussian_quadrature#Gauss%E2%80%93Legendre_quadrature

# if the weight is 1, its points are presumed to be 1/cbrt(3)
# and we have two points of x and two points of w

# the x values are on the range [-1, 1]
# weights can be defined by their points 1/cbrt(3)