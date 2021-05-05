import sympy as sy
import math as math
import mpmath
import three_b

a = sy.Symbol('a')
x = sy.Symbol('x')
h = 13.5
v = 20
g = 9.8065

# suppose a is 45 degrees, according to Eyob
# the answer will be 13.5 for a maximum distance
# let's check for this

top = g * x**2
sym_cos = sy.N(sy.cos(a).subs(a, mpmath.radians(a)))
sym_tan = sy.N(sy.tan(a).subs(a, mpmath.radians(a)))
bottom = 2*v**2*sym_cos**2
water_hose = top/bottom - sym_tan*x + h

#print(sy.solve(water_hose))

def get_angle_for_max_x(projection):
    max_distance = 0
    print("original function: " + str(projection))
    water_hose_diff = sy.diff(projection, a)
    print("function differentiated: " + str(water_hose_diff))
    simplify = sy.simplify(water_hose_diff)
    print("function simplified: " + str(simplify))

    # the launch function is v^2/g
    launch = pow(v, 2)/g
    # we get the angle we want the arctangent of
    angle = mpmath.degrees(1/sy.sqrt(1+2*h/launch))
    # arctangent will substitute the angle in the function
    tan_angle = sy.atan(angle)

    water_hose_replace_angle = water_hose_diff.subs(a, angle)
    # we get the distance by solving the projection equation
    max_distance = sy.solve(water_hose_replace_angle)

    return max_distance[1], angle

max_distance, angle = get_angle_for_max_x(water_hose)
print("The max distance is: " + str(max_distance))
print("The angle for this distance is: " + str(angle))


# couldn't figure out actual routine, so here's an alternative:
# https://physics.stackexchange.com/questions/23186/maximum-range-of-a-projectile-launched-from-an-elevation