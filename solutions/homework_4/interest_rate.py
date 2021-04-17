import math

epsilon = 1.0e-6

def secant(f, a, b, N):
    f0 = float(f(a))
    f1 = float(f(b))

    if f0*f1 >= 0:
        return

    while abs(a - b) >= epsilon:
        x2 = a - f1*(a - b)/(f1-f0)
        x0, x1 = x1, x2
        f0, f1 = f1, f(x1)
    return x2


def bisection(f, a, b, N):
    fa = f(a)
    fb = f(b)
    if f(a)*f(b) > 0:
        return
    n = (math.log(b-a) - math.log(epsilon))/(math.log(2))
    n = int(n)
    for i in range(n):
        c = a + 0.5*(b-a)
        fc = f(c)
        if fa*fc < 0:
            b = c
            fb = fc
        elif fa*fc > 0:
            a = c
            fa = fc
        else:
            a = c
        return a


def newton(f, fp, x0, N):
    if fp(x0) == 0:
        return

    x1 = x0 - f(x0)/fp(x0)
    i = 1
    while abs(x1 - x0) >= epsilon:
        i += 1
        x0 = x1
        fp0 = fp(x0)
        if i > 1000:
            return
        if fp0 == 0:
            return
        x1 = x0 - f(x0)/fp0

    return x1
