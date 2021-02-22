import math


def h(k):
    return pow(10, (-1*k))


def func(x):
    return math.tan(x)


def finite(x):
    values = []
    squared = []
    for i in range(0, 17):
        values.append((func(x + h(i)) - func(x))/h(i))
    return values, squared

def secx(x):
    values = []
    for i in range(0, 17):
        values.append(pow(math.sec(x), 2))
    return values

def centered(x):
    values = []
    squared = []
    for i in range(0, 17):
        values.append((func(x + h(i)) - func(x - h(i)))/(2*h(i)))
    return values


print("Finite-Difference Approximation results: \n" + str(finite(1)))
print("Centered-Difference Approximation results: \n" + str(centered(1)))
