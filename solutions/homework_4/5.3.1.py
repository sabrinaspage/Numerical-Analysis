from sympy import *
from scipy import e
import sympy

x = Symbol('x')

a1 = pow(x, 3) - 2*x - 5
b1 = pow(e, -x) - x
c1 = x*sin(x) - 1
d1 = x**3 - 3*x**2 - 1

a1_prime, b1_prime, c1_prime, d1_prime = (
    a1.diff(x), b1.diff(x), c1.diff(x), d1.diff(x))

tol = 1e-7
eps = 1e-14
solFound = False


def sign(a):
    return a > 0


def bisection(f, a, b, maxIter=50):
    n = 1
    while n <= maxIter:
        m = (a + b)/2
        if round(f.subs(x, m), 7) == 0:
            return m

        n += 1
        if sign(f.subs(x, m)) == sign(f.subs(x, a)):
            a = m
        else:
            b = m
    return 'max number of steps exceeded. diverges'


def newton(f, dF, x0, maxIter=20):
    for i in range(1, maxIter):
        y = f.subs(x, x0)
        yprime = dF.subs(x, x0)

        x1 = x0 - y/yprime
        if abs(x1 - x0) <= tol:
            return x1

        if abs(yprime) < eps:
            x1 = yprime
            break

        x0 = x1
    return x1


def secant(f, x0, x1, maxIter=10):
    for i in range(maxIter):
        x2 = x1 - f.subs(x, x1) * (x1 - x0) / \
            float(f.subs(x, x1) - f.subs(x, x0))
        x0, x1 = x1, x2
    return x2


def print_roots(f, val1, val2, val3):
    return "for {}, we have \nbisection root: {} \n\
newton root: {} \nsecant root: {} \n".format(f, val1, val2, val3)


a1_bi = bisection(a1, 1, 5)
a1_ne = newton(a1, a1_prime, 2)
a1_se = secant(a1, 0, 20)
print(print_roots(a1, a1_bi, N(a1_ne), a1_se), "\n")

b1_bi = bisection(b1, 1, 5)
b1_ne = newton(b1, b1_prime, 2)
b1_se = secant(b1, 0, 20, maxIter=5)
print(print_roots(b1, b1_bi, N(b1_ne), b1_se), "\n")

c1_bi = bisection(c1, 1, 3, maxIter=50)
c1_ne = newton(c1, c1_prime, 1.00, maxIter=4)
c1_se = secant(c1, 0, 5, maxIter=3)
print(print_roots(c1, c1_bi, str(N(c1_ne)), N(c1_se)), "\n")

d1_bi = bisection(d1, 1, 10)
d1_ne = newton(d1, d1_prime, 3, maxIter=40)
d1_se = secant(d1, 0, 20)
print(print_roots(d1, d1_bi, N(d1_ne), d1_se), "\n")

# using library routine

print("Root for {} with starting point {}: {}".format(a1, 0, nsolve(a1, 0)))
print("Root for {} with starting point {}: {}".format(b1, 0, nsolve(b1, 0)))
print("Root for {} with starting point {}: {}".format(c1, 0, nsolve(c1, 0)))
print("Root for {} with starting point {}: {}".format(d1, 3, nsolve(d1, 3)))
print("\n")

# attempt to get rate of convergence haha
# let's make a list to make it easy to visualize change in the sequence
# for every derived function

def sequence_list(f, n):
    terms = []
    for i in range(-n, n):
        term = N(f.subs(x, i))
        terms.append(term)
    return terms


a1_terms, b1_terms, c1_terms, d1_terms = (sequence_list(a1_prime, 20), sequence_list(
    b1_prime, 20), sequence_list(c1_prime, 20), sequence_list(d1_prime, 20))

print(a1_terms, b1_terms, c1_terms, d1_terms, sep="\n")
