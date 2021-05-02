import math
from sympy import *
import time
import scipy as sp
import scipy.optimize as scopt
import numpy as np

# constants
root_x = 2

# set up equations g1 to g4
x = Symbol('x')

g1 = (pow(x, 2) + 2)/3
g2 = sqrt(3*x - 2)
g3 = 3 - (2/x)
g4 = (pow(x, 2)-2)/(2*x-3)

# get their derivatives
g1_prime = g1.diff(x)
g2_prime = g2.diff(x)
g3_prime = g3.diff(x)
g4_prime = g4.diff(x)

print(g1_prime, g2_prime, g3_prime, g4_prime, sep='\n')
print('\n')

# answers are:
# 2*x - 3
# 2*x/3
# 3/(2*sqrt(3*x - 2))
# 2/x**2
# 2*x/(2*x - 3) - 2*(x**2 - 2)/(2*x - 3)**2

# plug in root for each answer:
g1_answer = g1_prime.subs(x, root_x)
g2_answer = g2_prime.subs(x, root_x)
g3_answer = g3_prime.subs(x, root_x)
g4_answer = g4_prime.subs(x, root_x)

print(g1_answer, g2_answer, g3_answer, g4_answer, sep='\n')
print('\n')

# check for convergence

def check_for_convergence(g, x):
    if x < 1:
        return '{} converges for {} < 1'.format(g, x)
    else:
        return '{} diverges for {} > 1'.format(g, x)

g1_conv = check_for_convergence(g1_prime, g1_answer)
g2_conv = check_for_convergence(g2_prime, g2_answer)
g3_conv = check_for_convergence(g3_prime, g3_answer)
g4_conv = check_for_convergence(g4_prime, g4_answer)

print(g1_conv, g2_conv, g3_conv, g4_conv, sep='\n')
print("\n")

# check for convergence rate of convergent functions
# we want |e(n + 1)|/|e(n)|^r
# r is the order of convergence

n = Symbol('n')
r = Symbol('r')

g2_n_1 = sqrt((3 * (n + 1)) - 2)
g3_n_1 = 3 - (2/(n + 1))
g4_n_1 = (pow((n + 1), 2) - 2)/(2 * (n + 1) - 3)

g2_n_r = sqrt((3 * n) - 2)**r
g3_n_r = (3 - (2/n))**r
g4_n_r = ((pow(n, 2) - 2)/(2 * n - 3))**r

print("|e(n + 1)|: \n", g2_n_1, g3_n_1, g4_n_1, sep="\t")
print("\n")
print("|e(n)|^r: \n", g2_n_r, g3_n_r, g4_n_r, sep="\t")
print("\n")

g2_method = g2_n_1/g2_n_r
g3_method = g3_n_1/g3_n_r
g4_method = g4_n_1/g4_n_r

print("|e(n + 1)|/|e(n)|:", g2_method, g3_method, g4_method, sep="\n")
print("\n")

# function for rate of convergence

def rate_of_conv(func, rate_of_conv, epsilon):
    new_func = func.subs(r, rate_of_conv)
    print(new_func)
    for inc in range(1, epsilon):
        func = N(new_func.subs(n, inc))
    return func
    
        
# check for rate of convergence
# all the members of each of the following sequences are the
# magnitudes of the errors at successive iterations of an
# iterative method (in this case, linear), we can assume the
# results here: 
g2_constant = math.floor(rate_of_conv(g2_method, 1, 100))
print("if g2 is linear, then r = 1, and constant will approach: " + str(g2_constant))
print("\n")

g3_constant = math.floor(rate_of_conv(g3_method, 5, 100))
print("if g3 is linear, then r = 1, and constant will approach: " + str(g3_constant))
print("\n")

g4_constant = math.floor(rate_of_conv(g4_method, 1, 100))
print("if g3 is linear, then r = 1, and constant will approach: " + str(g4_constant))