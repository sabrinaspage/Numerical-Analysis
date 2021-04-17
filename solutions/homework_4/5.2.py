import math
from sympy import *
import time
import scipy as sp
import scipy.optimize as scopt

###### 5.2b. I hope I did this correctly?!

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

# Hopefully this is all we have to do for 5.2a and 5.2b?!