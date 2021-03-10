import math
import os

# system call
os.system("")


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# recall the summation of e^x is the summation starting from n = 0 to k
# where k is either an exact number or infinity; and i increments from n to k
# and x^i is divided by factorial of i aka x^i/i!


n = 0
k = 100


def power(base, k):
    res = 1
    for i in range(k):
        res *= base
    return res


def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


def exp_series(start, end):
    result = 0
    for i in range(start, end):
        result += power(x, i) / factorial(i)
    return result


arr = [-20, 20, -15, 15, -10, 10, -5, 5, -1, 1]

for x in arr:
    user_defined = exp_series(n, k)
    math_defined = math.exp(x)
    result = user_defined - math_defined

    print(style.YELLOW + "For e^" + str(x) +
          " using user created functions: ", user_defined)
    print(style.RED + "Using exp(" + str(x) +
          ") from math library: " + str(math_defined))
    print(style.CYAN + "The difference between user_defined and exp(): " + str(result))
    print(style.WHITE + "#--------------")

for x in arr:
    if x > 0:
        div_math_defined = 1/math.exp(x)
        print(style.WHITE + "Using 1/exp(" + str(x) +
              ") from math library: " + str(div_math_defined))

for x in arr:
    if x > 0:
        div_user_defined = 1/exp_series(n, k)
        print(style.WHITE + "Using 1/exp_series(" + str(x) +
              ") from math library: " + str(div_user_defined))
