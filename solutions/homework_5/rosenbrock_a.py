from sympy import *
from matplotlib.pyplot import *

epsilon = 10^-2
x1 = Symbol('x1')
x2 = Symbol('x2')

rosenbrock = 100*pow((x2 - pow(x1, 2)), 2) + pow((1 - x1), 2)
start_1 = (-1, 1)
start_2 = (0, 1)
start_3 = (2, 1)

def get_first_partial_derivatives(function):
    f_x1 = diff(function, x1)
    f_x2 = diff(function, x2)

    return [f_x1, f_x2]

def get_critical_points(function):
    gradient = get_first_partial_derivatives(function)
    critical_points = solve(gradient, [x1, x2])

    return critical_points[0]

def get_second_partial_derivatives(gradient):
    gradient_of_x1 = get_first_partial_derivatives(gradient[0])
    fx1x1 = gradient_of_x1[0]
    fx2x1 = gradient_of_x1[1]

    gradient_of_x2 = get_first_partial_derivatives(gradient[1])
    fx1x2 = gradient_of_x2[0]
    fx2x2 = gradient_of_x2[1]

    return fx1x1, fx2x1, fx1x2, fx2x2

def second_partial_derivative_test(derivatives, point):
    fxx, fyx, fxy, fyy = derivatives
    H = fxx * fyy - fxy * fyx
    subs_H = H.subs(x1, point[0]).subs(x2, point[1])
    if subs_H < 0:
        return str(subs_H) + " is a saddle point."
    elif subs_H == 0:
        return "Not enough information."
    else:
        subs_fxx = fxx.subs(x1, point[0]).subs(x2, point[1])
        if subs_fxx < 0:
            return "Critical point is a local maximum point."
        else:
            return "Critical point is a local minimum point."

def steepest_descent(function, starting_point, learning_rate=0.001):
    gradient = get_first_partial_derivatives(function)
    func_with_start = function.subs(x1, starting_point[0]).subs(x2, starting_point[1])
    
    to_change = starting_point
    count = 0

    to_minimized = []
    to_convergence = []
    while func_with_start >= 0.01:
        print(func_with_start)
        to_minimized.append(to_change)
        func_with_start = function.subs(x1, to_change[0]).subs(x2, to_change[1])
        first_partial_with_start = gradient[0].subs(x1, to_change[0]).subs(x2, to_change[1])
        second_partial_with_start = gradient[1].subs(x1, to_change[0]).subs(x2, to_change[1])

        minimize_x1 = to_change[0] - learning_rate*first_partial_with_start
        minimize_x2 = to_change[1] - learning_rate*second_partial_with_start
        to_change = (minimize_x1, minimize_x2)
        to_convergence.append(func_with_start)
        count += 1

    return to_minimized, to_convergence, f"It takes {count} iterations to converge to the critical point of {function} with a learning rate of {learning_rate}, starting at {starting_point}"

def plot_steepest(function, starting_point, learning_rate=0.01):
    path, convergence, description = steepest_descent(function, starting_point, learning_rate)
    
    x1_list = []
    x2_list = []
    for x in path:
        x1_list.append(x[0])
        x2_list.append(x[1])

    fig, (path_graph, convergence_graph) = subplots(1, 2)
    path_graph.plot(x1_list, label = "Changes in x1")
    path_graph.plot(x2_list, label = "Changes in x2")
    path_graph.set_title('Changes in x1, x2 Until Minimized for f(x1, x2) - Rosenbrock')
    path_graph.set(xlabel='iterations', ylabel='values of x')

    convergence_graph.plot(convergence)
    convergence_graph.set_title('Plotting to Convergence of f(x1, x2) - Rosenbrock')
    convergence_graph.set(xlabel='iterations', ylabel='values of f(x1, x2)')
    
    fig.suptitle(description)

    path_graph.legend()
    show()

critical_point = get_critical_points(rosenbrock)
first_gradient = get_first_partial_derivatives(rosenbrock)
second_gradient = get_second_partial_derivatives(first_gradient)
check = second_partial_derivative_test(second_gradient, critical_point)

# https://mathworld.wolfram.com/RosenbrockFunction.html
# rosenbrock has a global
# minimum of 0 at the point (1, 1)

print(critical_point, first_gradient, second_gradient, check, sep="\n")
plot_steepest(rosenbrock, start_1, learning_rate=0.001)
plot_steepest(rosenbrock, start_2, learning_rate=0.0001)
plot_steepest(rosenbrock, start_3, learning_rate=0.001)