from sympy import *
from sympy.matrices import *
from matplotlib.pyplot import *
from pandas import *
import operator
from _decimal import Decimal
import numpy as np
from matplotlib import pyplot as plt

x1 = Symbol('x1')
x2 = Symbol('x2')
rosenbrock = 100*pow((x2 - pow(x1, 2)), 2) + pow((1 - x1), 2)

start_1 = [-1, 1]
start_2 = [0, 1]
start_3 = [2, 1]


def get_gradient(function):
    """
    Find the gradient of the function
    """
    f_x1 = diff(function, x1)
    f_x2 = diff(function, x2)

    return [f_x1, f_x2]

def gradient_subs(gradient, point):
    """
    Substitute the gradient with some point
    """
    f_x1 = gradient[0].subs(x1, point[0]).subs(x2, point[1])
    f_x2 = gradient[1].subs(x1, point[0]).subs(x2, point[1])

    return [f_x1, f_x2]

def matrix_subs(matrix_2x2, point):
    """
    Substitute a Sympy matrix with some points
    """
    arr = []
    for el in matrix_2x2:
        arr.append(el.subs(x1, point[0]).subs(x2, point[1]))
    
    M = Matrix([[arr[0], arr[1]], [arr[2], arr[3]]])

    return M

def get_jacobian(gradient):
    """
    Get the Jacobian matrix from a gradient; or two functions in a 1d array
    """
    gradient_of_x1 = get_gradient(gradient[0])
    fx1x1 = gradient_of_x1[0]
    fx2x1 = gradient_of_x1[1]

    gradient_of_x2 = get_gradient(gradient[1])
    fx1x2 = gradient_of_x2[0]
    fx2x2 = gradient_of_x2[1]

    M = Matrix([[fx1x1, fx2x1], [fx1x2, fx2x2]])

    return M

def Ax_b(A, b):
    """
    Compute x for Ax=b with a linear system solving mechanism
    """
    x = Matrix([x1, x2])
    Ax = A*x
    Ax_b = Ax - b
    x = linsolve([Ax_b[0], Ax_b[1]], x1, x2)
    return tuple(*x)

def newtons_method(function, start, epsilon_rounding=6):
    """
    Newton's method.

    If you're wondering, or reading this, I initially replicated the example
    in the textbook (page 238). Once I was able to initialize a basis step,
    I then wrote a while loop to iterate until it met a condition.
    That condition being, if at some point the result of the previous iteration
    is the same as the current one, return - because there is no need to
    continue.

    :param function -- accepts the rosenbrock function, or assumingly any multivariate function
    :param start -- starting point
    :param epsilon_rounding -- essentially multiplies the result of the points with 10^-6, so we don't
        iterate past it
    """
    point = start

    f = get_gradient(function)
    jacobian_matrix = get_jacobian(f)
    inverse_jacobian = jacobian_matrix.inv()

    f_subs = gradient_subs(f, point)

    temp = [0, 0]

    points = [point]
    while temp != point:
        jacobian_subs_matrix = matrix_subs(jacobian_matrix, point)
        inverse_subs_jacobian = matrix_subs(inverse_jacobian, point)
        negative_gradient = Matrix([-x for x in f_subs])
        solution = Ax_b(jacobian_subs_matrix, negative_gradient)
        temp = [round(float(x), epsilon_rounding) for x in point]
        point = [a + b for a, b in zip(solution, point)]
        point = [round(float(x), epsilon_rounding) for x in point]
        points.append(point)
        f_subs = gradient_subs(f, point)
        new_minimum = [float(x) for x in point]

    return new_minimum, points, f"The minimum is {new_minimum}, with a starting point of {start}"

# with the help of this handy URL
# http://et.engr.iupui.edu/~skoskie/ECE580/ECE580_PS4soln_s16.pdf
# and page 238 of the textbook

def plot_path(function, starting_point):
    path, convergence, description = newtons_method(function, starting_point)
    x = np.linspace(-4, 4, 100)
    y = np.linspace(-4, 4, 100)

    X, Y = np.meshgrid(x, y)
    Z = X**2 + Y**2
    plt.contour(X, Y, Z, 10)

    x1_list = []
    x2_list = []
    for x in convergence:
        x1_list.append(x[0])
        x2_list.append(x[1])

    plt.plot(x1_list, x2_list, '-')
    plt.axis('square')
    plt.title(description)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

plot_path(rosenbrock, start_1)
plot_path(rosenbrock, start_2)
plot_path(rosenbrock, start_3)

print(newtons_method(rosenbrock, start_1))
print(newtons_method(rosenbrock, start_2))
print(newtons_method(rosenbrock, start_3))

