import math
import mpmath
import pylab
import numpy as np
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


def centered(x):
    values = []
    errors = []
    for i in range(0, 17):
        values.append((math.tan(x + h(i)) - math.tan(x - h(i)))/(2*h(i)))
    for i in range(len(values)):
        errors.append(abs(sec2 - values[i]))
    return values, errors


centered_vals, centered_errs = centered(const_x)

df = pd.DataFrame({"Centered-Diff Approx.": centered_vals,
                   "Centered-Diff Errors": centered_errs})
df['Centered-Diff Approx.'] = df['Centered-Diff Approx.'].map(
    lambda x: '%2.16f' % x)

print(df)
print("Lowest level in magnitude of error (h): " + str(min(centered_errs)))
print("Machine epsilon has a value of: " + str(np.finfo(float).eps))
print("The approximate value of h, h≈sqrt(emach), in exercise 1.3, is: " +
      str(math.sqrt(np.finfo(float).eps)))

print("When h is at 10^-7, the minimum error is lower than the finite error, occurring at 10^12." +
      " 10^7 is slightly bigger than the value of h.")

fig = plt.figure()
ax = fig.add_subplot()

line, = ax.plot(x_axis(), centered_errs, color='blue', lw=2)
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_title("Centered-Difference Approximate Value Errors")
ax.set_xlabel("h^i where i = [0, 16]")
ax.set_ylabel("Magnitude of Error")

pylab.show()
