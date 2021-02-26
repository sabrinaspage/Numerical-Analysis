import math
import mpmath
import numpy as np
import pylab
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as mtick

const_x = 1
sec2 = mpmath.sec(const_x)*mpmath.sec(const_x)


def h(k):
    return pow(10, (-1*k))

def x_axis():
    values = []
    for i in range(0, 17):
        values.append(h(i))
    return values


def finite(x):
    values = []
    errors = []
    for i in range(0, 17):
        values.append((math.tan(x + h(i)) - math.tan(x))/h(i))
    for i in range(len(values)):
        errors.append(abs(sec2 - values[i]))
    return values, errors


finite_vals, finite_errs = finite(const_x)

df = pd.DataFrame({"Finite-Diff Approx.": finite_vals, "Finite-Diff Errors": finite_errs})
df['Finite-Diff Approx.'] = df['Finite-Diff Approx.'].map(lambda x: '%2.16f' % x)

print(df)
print(x_axis())

print("Lowest level in magnitude of error (h): " + str(min(finite_errs)))
print("Machine epsilon has a value of: " + str(np.finfo(float).eps))
print("The approximate value of h, h≈sqrt(emach), in exercise 1.3, is: " + str(math.sqrt(np.finfo(float).eps)))

print("The lowest value of h in finite-difference approximation and h in example 1.3, h≈sqrt(emach), is that they both happen at 10^-8")

fig = plt.figure()
ax = fig.add_subplot()

line, = ax.plot(x_axis(), finite_errs, color='blue', lw=2)

ax.set_yscale('log')
ax.set_xscale('log')
ax.set_title("Finite-Difference Approximate Value Errors")
ax.set_xlabel("h^i where i = [0, 16]")
ax.set_ylabel("Magnitude of Error")

pylab.show()