from sympy import *
from scipy import e

x = Symbol('x')

a1 = pow(x, 3) - 2*x - 5
b1 = pow(e, -x) - x
c1 = x*sin(x) - 1
d1 = pow(x, 3) - 3*pow(x, 2) - 1

a1_prime = a1.diff(x)
b1_prime = b1.diff(x)
c1_prime = c1.diff(x)
d1_prime = d1.diff(x)

# let's analyze the convergence properties of each fixed-point iteration
# scheme with Newton's method and get their convergence rates

# consider these properties:
# if method is not guaranteed to converge, set a maximum number of iterations
# stopping criteria: we don't know how close we are to a solution - all we can
# computer is the value f(x), so we implement a stopping criteria based on f(x)
# we must compute values of derivative

# so we write a function called newton which takes five input parameters
# f, Df, x0, epsilon, and max_iter
# return an approximation of a solution of f(x) = 0

# termination occurs when we find an approximate solution:
# the absolute value of the function is less than epsilon, so we have an approx value
# if we have the zero derivative, so no solution is found
# we exceed the max iterations, and we return no solution

def newton(f, Df, x0, epsilon, max_iter):
    xn = x0
    for n in range(0, max_iter):
        fxn = f.subs(x, xn)
        if (abs(fxn)) < epsilon:
            return 'Found solution {} after {} iterations. Converges'.format(xn, n)
        Dfxn = Df.subs(x, xn)
        if Dfxn == 0:
            #Zero derivative. No solution found.
            return None
        xn = xn - fxn/Dfxn
    #Exceeded maximum iterations. No solution found. Diverges
    return None

#### simplest root finding algorithm is the bisection method
# applies to any continuos function f(x) on an interval [a, b]
# value of function f(x) changes sign from a to b
# divide interval in two - a solution exists within one subinterval

### generally, the procedure is as such:
# 1. we have a starting interval [a0, b0], f(a0)f(b0)<0
# 2. f(m0) where m0 = (a0 + b0)/2 is the midpoint
# Determine the next subinterval :
# If f(a0)f(m0) < 0, then let [a1, b1] be the next interval with a1=a0 and b1=m0.
# If f(b0)f(m0) < 0, then let  be the next interval with a1=m0 and b1=b0.
# Repeat (2) and (3) until the interval [aN, bN] reaches some predetermined length.
# Return the midpoint value mN=(aN+bN)/2.

# a solution to the equation f(x) = 0 in the interval [a, b] is guaranteed by
# IVT. function changes sign over the interval and must equal 0 at some point

# we do not need an exact equation of f(x) = 0, just an estimate

def bisection(f, a, b, epsilon):
    if f.subs(x, a)*f.subs(x, b) >= 0:
        return None
    a_n = a
    b_n = b
    for n in range(1,epsilon+1):
        c = (a_n + b_n)/2
        f_m_n = f.subs(x, c)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = c
        elif f(b_n)*f_m_n < 0:
            a_n = c
            b_n = b_n
        elif f_m_n == 0:
            return c
        else:
            return None
    return (a_n + b_n)/2

### secant method - find the root of an equation f(x) = 0
# starts from two distinct estimates x1 and x2 for the root
# iterative procedure involving linear interpolation to a root.
## if the difference between two intermediate values < convergence factor
# iteration stops

def secant(f, x1, x2, epsilon):
    f1 = float(f.subs(x, x1))
    f2 = float(f.subs(x, x2))
    n = 1

    while abs(x2 - x1) >= epsilon:
        n += 1
        x3 = x2 - f2*(x2-x1)/(f2-f1)
        x1, x2 = x2, x3
        f1, f2 = f2, f.subs(x, x2)
    return x3

#########################

a1_root = 2

print(newton(a1, a1_prime, a1_root, 1e-06, 100))
print(bisection(a1, 0, 5, 1e-06))
print(secant(a1, 0, 5, 1e-06))

print(newton(a1, a1_prime, a1_root, 1e-06, 100))
print(bisection(a1, 0, 5, 1e-06))
print(secant(a1, 0, 5, 1e-06))

print(newton(a1, a1_prime, a1_root, 1e-06, 100))
print(bisection(a1, 0, 5, 1e-06))
print(secant(a1, 0, 5, 1e-06))

print(newton(a1, a1_prime, a1_root, 1e-06, 100))
print(bisection(a1, 0, 5, 1e-06))
print(secant(a1, 0, 5, 1e-06))