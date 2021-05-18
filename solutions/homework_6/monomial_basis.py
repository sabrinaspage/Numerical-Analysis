import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import math as m
from scipy.interpolate.interpolate import lagrange

x = np.array([0, 1, 4, 9, 16, 25, 36, 49, 64])

poly = lagrange(x, [m.sqrt(i) for i in x])
cs = CubicSpline(x, [m.sqrt(i) for i in x])
xs = np.arange(0, 64.2, 0.2)

plt.plot(x, [m.sqrt(i) for i in x], 'o', label='data')
plt.plot(xs, cs(xs), label="Cubic Spline", linewidth=0.5)
plt.plot(xs, poly(xs), label="Monomial Basis", linewidth=0.5)
plt.legend(loc='best', ncol=2)
plt.title("Cubic Spline vs Monomial Basis")
plt.xlim(0, 1.4)
plt.ylim(0, 1.2)
plt.xlabel("t")
plt.ylabel("sqrt(t)")
plt.show()