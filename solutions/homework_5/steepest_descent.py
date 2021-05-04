from sympy import *
from matplotlib.pyplot import *

epsilon = 10**-3
x1 = Symbol('x1')
x2 = Symbol('x2')

function = 5*pow(x1, 2) + 5*pow(x2, 2) - x1*x2 - 11*x1 + 11*x2 + 11
example = 0.5*pow(x1, 2) + 2.5*pow(x2, 2)

# in order to get the first-order necessary conditions
# we must get the critical point where the gradient of f(x*) = 0
# get df/dx1, df/dx2; in other words, fx1 and fx2

print("Function we are working with: ", function)

def get_first_partial_derivatives(function):
    f_x1 = diff(function, x1)
    f_x2 = diff(function, x2)

    return [f_x1, f_x2]

print("Gradient of the function: ", get_first_partial_derivatives(function))

def get_critical_points(function):

    gradient = get_first_partial_derivatives(function)
    critical_points = solve(gradient, [x1, x2])
    return critical_points

print("Critical points of the function: ", get_critical_points(function))

# in order to determine that this point is the global minimum
# check for the derivative of the gradient, which verifies
# whether this is a local maximum, local minimum, or saddle point
# btw, since this is the only point we're looking at, we can assume
# it is either a global min or global max

# we have already determined fx1 and fx2
# now we can take the partial derivatives of the gradient
# for:
# fx1x1, fx2x1, fx1x2, fx2x2

def get_second_partial_derivatives(gradient):
    gradient_of_x1 = get_first_partial_derivatives(gradient[0])
    fx1x1 = gradient_of_x1[0]
    fx2x1 = gradient_of_x1[1]

    gradient_of_x2 = get_first_partial_derivatives(gradient[1])
    fx1x2 = gradient_of_x2[0]
    fx2x2 = gradient_of_x2[1]

    return fx1x1, fx2x1, fx1x2, fx2x2

derivs = get_second_partial_derivatives(get_first_partial_derivatives(function))
print("Second partial derivatives of the function: ", derivs)

# compute this quantity for the second partial derivative test:
# H = fxx(x0, y0)*fyy(x0, y0)-fxy(x0, y0)^2

def second_partial_derivative_test(derivatives):
    fxx, fyx, fxy, fyy = derivatives
    H = fxx * fyy - fxy * fyx
    if H < 0:
        return str(H) + " is a saddle point."
    elif H == 0:
        return "Not enough information."
    else:
        if fxx < 0:
            return "Critical point is a local maximum point."
        else:
            return "Critical point is a local minimum point."

print("Given that there is only one local point, we can call this the global max/min")
print(second_partial_derivative_test(derivs))

# given that we only retrieve one critical point, we can assume the
# local minimum is the global minimum

# sources:
# http://liberzon.csl.illinois.edu/teaching/cvoc/node7.html
# https://www.khanacademy.org/math/multivariable-calculus/applications-of-multivariable-derivatives/optimizing-multivariable-functions/a/g/a/maximums-minimums-and-saddle-points
# https://www.khanacademy.org/math/multivariable-calculus/applications-of-multivariable-derivatives/optimizing-multivariable-functions/a/g/a/second-partial-derivatives
# https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/partial-derivative-and-gradient-articles/a/second-partial-derivatives

# -----------------------------------------------------------
# we know a function converges if, as x increases, the function
# approaches some constant

# if we start at 0, 0
x = (0, 0)

def steepest_descent(function, starting_point, learning_rate=0.1):
    gradient = get_first_partial_derivatives(function)
    func_with_start = function.subs(x1, starting_point[0]).subs(x2, starting_point[1])
    
    to_change = starting_point
    count = 0

    to_minimized = []
    to_convergence = []
    while func_with_start >= epsilon:
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

# sources:
# page 276 of textbook
# https://towardsdatascience.com/machine-learning-bit-by-bit-multivariate-gradient-descent-e198fdd0df85

# plot the points on a graph

def plot_steepest(starting_point):
    path, convergence, description = steepest_descent(function, starting_point)
    
    x1_list = []
    x2_list = []
    for x in path:
        x1_list.append(x[0])
        x2_list.append(x[1])

    fig, (path_graph, convergence_graph) = subplots(1, 2)
    path_graph.plot(x1_list, label = "Changes in x1")
    path_graph.plot(x2_list, label = "Changes in x2")
    path_graph.set_title('Changes in x1, x2 Until Minimized for f(x1, x2)')
    path_graph.set(xlabel='iterations', ylabel='values of x')

    convergence_graph.plot(convergence)
    convergence_graph.set_title('Plotting to Convergence of f(x1, x2)')
    convergence_graph.set(xlabel='iterations', ylabel='values of f(x1, x2)')

    fig.suptitle(description)
    
    path_graph.legend()
    show()

plot_steepest((2,3))
plot_steepest((2,1))
plot_steepest((1,1))
