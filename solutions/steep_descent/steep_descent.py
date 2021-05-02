import numpy as np
import matplotlib.pyplot as plt
from ad import *
from sympy import *

first_theta = 10
second_theta = 100
epsilon = 10e-6

x0_x_1, x0_y_1 = (8, 90)
x0_x_2, x0_y_2 = (1, 40)
x0_x_3, x0_y_3 = (15, 68.69)
x0_x_4, x0_y_4 = (10, 20)

x1 = Symbol('x1', real=True)
x2 = Symbol('x2', real=True)
theta = Symbol('theta', real=True)

func = -9 * x1 - 10 * x2 + theta * (-ln(100 - x2 - x2) - ln(x1) - ln(x2) - ln(50 - x1 + x2))

def steepest_descent(f, tol, x, y, f_theta):
    f_old = 9999
    x_1, x_2 = np.array(x, y)
    steps = []
    f_new = f.subs(x1, x_1).subs(x2, x_2).subs(theta, f_theta)
    print(N(f_new))
    
    while abs(f_old - f_new) > epsilon:
        f_old = f_new
        d = -np.array(gh(f)[0](x_1))
        x = x + d * 1
        f_new = f(x)
        steps.append(list(x1, x2))
    return x, f_new, steps
    
steepest_descent(func, epsilon, x0_x_1, x0_y_1, first_theta)
steepest_descent(func, epsilon, x0_x_1, x0_y_1, second_theta)
