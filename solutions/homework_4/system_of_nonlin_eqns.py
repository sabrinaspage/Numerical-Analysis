import sympy
from sympy import Symbol, solve, nsolve

x1 = Symbol('x1')
x2 = Symbol('x2')
w1 = Symbol('w1')
w2 = Symbol('w2')

eq1 = w1 + w2
eq2 = (w1 * x1) + (w2 * x2)
eq3 = (w1 * pow(x1, 2)) + (w2 * pow(x2, 2))
eq4 = (w1 * pow(x1, 3)) + (w2 * pow(x2, 3))

print(nsolve((eq1, eq2, eq3, eq4)), (x1, x2, w1, w2), (2, 0, 2/3, 0))
