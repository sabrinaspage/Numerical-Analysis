import math
import mpmath
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
    for i in range(17, 0, -1):
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

plt.title('Difference Functions')

plt.plot(x_axis(), finite_errs, label='Finite-Difference Errors at x=1')

plt.ticklabel_format(axis='both', style='sci', scilimits=(4, 4))

plt.xlabel("Values of i = [0,17] on h^(i)")
plt.ylabel("Magnitude of Error")

plt.legend()
plt.show()
