import numpy as np
from matplotlib import pyplot as plt

def poly6(x):
    return pow(x-1, 6)

def expanded(x):
    first = pow(x, 6)
    second = 6*pow(x, 5)
    third = 15*pow(x, 4)
    fourth = 20*pow(x, 3)
    fifth = 15*pow(x, 2)
    sixth = 6*x
    seventh = 1
    return first - second + third - fourth + fifth - sixth + seventh

interval = np.arange(0.995, 1.005, 0.0001)
poly_interval = []
expanded_interval = []

for i in interval:
    poly_interval.append(poly6(i))
    expanded_interval.append(expanded(i))

plt.title('Polynomial Comparison')

plt.plot(poly_interval, label='Polynomial (x-1)^6')
plt.plot(expanded_interval, label='Expanded Polynomial for (x-1)^6')

plt.xlabel("Number of Values in Interval [0.995, 1.005]")
plt.ylabel("Resulting Numbers of Polynomials")

x = np.random.randint(low=0, high=50, size=100)

plt.xticks(np.arange(0, len(x)+1, 10))

plt.legend()
plt.show()
