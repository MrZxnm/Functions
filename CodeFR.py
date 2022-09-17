"""
A set of functions for finding all roots (including complex ones) of equations
of the type a*x + b = 0, a*x^2 + b*x + c = 0 and a*x^3 + b*x^2 + c*x + d = 0.
By default, all coefficients except "a" are equal to zero.
Coefficient "a" must not be equal to 0.
"""
def find_roots_1(a, b = 0):
    "Solves a linear equation (a*x + b = 0)."
    if a == 0: raise ZeroDivisionError('"a" must not be zero.')
    return complex(-b/a)
def find_roots_2(a, b = 0, c = 0):
    "Solves a quadratic equation (a*x^2 + b*x + c = 0)."
    if a == 0: raise ZeroDivisionError('"a" must not be zero.')
    D = complex(b**2 - 4*a*c)
    return complex((-b + D**(1/2))/(2*a)), complex((-b - D**(1/2))/(2*a))
def find_roots_3(a, b = 0, c = 0, d = 0):
    "Solves a cubic equation (a*x^3 + b*x^2 + c*x + d = 0)."
    if a == 0: raise ZeroDivisionError('"a" must not be zero.')
    p = complex((3*a*c - b**2)/(3*a**2))
    q = complex((27*a**2*d - 9*a*b*c + 2*b**3)/(27*a**3))
    Q = complex((p/3)**3 + (q/2)**2)
    alpha = complex((-q/2 + Q**(1/2))**(1/3))
    beta = complex(-p/(alpha*3))
    return complex(alpha + beta - b/(3*a)), complex(-(alpha + beta)/2 + (-3)**(1/2)*(alpha - beta)/2 - b/(3*a)), complex(-(alpha + beta)/2 - (-3)**(1/2)*(alpha - beta)/2 - b/(3*a))
