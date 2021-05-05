import sympy as sy
import math as math
from mpmath import *

a = 70
x = sy.Symbol('x')
h = 13.5
v = 20
g = 9.8065
epsilon = 10**-7

top = g * x**2
bottom = 2*v**2*sy.cos(math.radians(a))**2
water_hose = top/bottom - sy.tan(math.radians(a)) * x + h

def df(f, x):
    h = 1e-5
    return (f.subs(x, x + h) - f.subs(x, x))/h

def newtons(function, start):
    sol = False
    x0 = start
    yprime = df(function, x).subs(x, x0)

    while abs(yprime) >= epsilon:
        y = function.subs(x, x0)
        yprime = df(function, x).subs(x, x0)

        x1 = x0 - y/yprime

        if abs(x1-x0) <= epsilon:
            sol = True
            break

        x0 = x1

    if sol:
        return x0
    else:
        return "Did not converge"

print("Maximum distance: " + str(newtons(water_hose, 19)))

# to be imported by question 3c
max_distance = newtons(water_hose, 19)