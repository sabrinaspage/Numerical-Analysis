import math as m
from sympy import *

n = Symbol('n')
a = Symbol('a')
r = Symbol('r')
p = Symbol('p')

repaid = a * pow((1 + r), n)
yearly = p * (pow((1 + r), n) - 1)/r


def samesign(a, b):
    """
        if the functions values are both the same, return true.
        if the values are different, return false.
    """
    return a * b > 0


def bisection(f, g, to_update, a, b):
    tol = 0

    # if the end points make the functions equal, return those
    if round(f.subs(to_update, a), 2) == round(g.subs(to_update, a), 2):
        return a

    if round(f.subs(to_update, b), 2) == round(g.subs(to_update, b), 2):
        return b

    while b - a > tol:
        mid = a + (b-a)/2

        f_val = f.subs(to_update, mid)
        g_val = g.subs(to_update, mid)

        print(f_val, g_val, mid)

        # return the midpoint where the truncated values of the function match
        if round(f_val, 2) == round(g_val, 2):
            return 'Total amount repaid is {}. Yearly payments would reduce this amount at {}. \
Loan is paid off when {} is {}'.format(round(f_val), round(g_val), n, mid)
        else:
            if f_val > g_val:
                a = mid
            else:
                b = mid

    if b - a <= tol:
        return 'Loan is never paid off'


def bisection(f, g, to_update, a, b):
    tol = 0

    orig_a = a
    orig_b = b

    # if the end points make the functions equal, return those
    if round(f.subs(to_update, a), 2) == round(g.subs(to_update, a), 2):
        return a

    if round(f.subs(to_update, b), 2) == round(g.subs(to_update, b), 2):
        return b

    while b - a > tol:
        mid = a + (b-a)/2

        f_val = f.subs(to_update, mid)
        g_val = g.subs(to_update, mid)

        # return the midpoint where the truncated values of the function match
        if round(f_val, 2) == round(g_val, 2):
            return 'Total amount repaid is {}. Yearly payments would reduce this amount at {}. \
Loan is paid off when {} is {}'.format(round(f_val), round(g_val), n, mid)
        else:
            if f_val > g_val:
                a = mid
            else:
                b = mid

    if b - a <= tol:
        return 'Total amount repaid is {}. Yearly payments would reduce this amount at {}. \
Loan is never paid off because the values are not equal. r approached {} on an interval from \
[{},{}]'.format(f_val, g_val, mid, orig_a, orig_b)

def answer_a(a_val=100000, r_val=0.06, p_val=10000):
    repaid_num = repaid.subs(a, a_val).subs(r, r_val)
    yearly_num = yearly.subs(a, a_val).subs(p, p_val).subs(r, r_val)

    print('repaid function: ' + str(repaid_num), 'reduce function: ' + str(yearly_num), sep="\n")
    print(bisection(repaid_num, yearly_num, n, 15, 16), "\n")


def answer_b(a_val=100000, n_val=20, p_val=10000):
    repaid_num = repaid.subs(a, a_val).subs(n, n_val)
    yearly_num = yearly.subs(a, a_val).subs(n, n_val).subs(p, p_val)

    print('repaid function: ' + str(repaid_num), 'reduce function: ' + str(yearly_num), sep="\n")
    print(bisection(repaid_num, yearly_num, r, 1, 10000), "\n")


def answer_c(a_val=100000, n_val=20, r_val=0.06):
    repaid_num = repaid.subs(a, a_val).subs(r, r_val).subs(n, n_val)
    yearly_num = yearly.subs(a, a_val).subs(r, r_val).subs(n, n_val)

    print('repaid function: ' + str(repaid_num), 'reduce function: ' + str(yearly_num), sep="\n")
    # we don't need to apply a method because repaid_num already is a value

    x = solve(yearly_num - repaid_num, p)

    print('the yearly payments {} must be {}'.format(p, x[0]))

def main():
    answer_a()
    answer_b()
    answer_c()

if __name__ == '__main__':
    main()
