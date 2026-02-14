import math

def newton_method(func, derivative, x0, tolerance = 1e-6, max_iter = 1000):
    for i in range(max_iter):
        x1 = x0 - func(x0) / derivative(x0)
        if abs(x1 - x0) < tolerance:
            return x1, i + 1
        x0 = x1
    return x0, max_iter

def secant(func, x0, x1, tolerance = 1e-6, max_iter = 1000):
    for i in range(max_iter):
        x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        if abs(x2 - x1) < tolerance:
            return x2, i + 1
        x0, x1 = x1, x2
    return x1, max_iter

def bisection(func, a, b, tolerance = 1e-6, max_iter = 1000):
    if func(a) * func(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    for i in range(max_iter):
        c = (a + b) / 2
        if abs(func(c)) < tolerance or (b - a) / 2 < tolerance:
            return c, i + 1
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2, max_iter

functions = {
    "a": (lambda x: 1 - 2*x*math.exp(-x/2),
          lambda x: -2*math.exp(-x/2) + x*math.exp(-x/2)),
    "b": (lambda x: 5 - 1/x,
          lambda x: 1/x**2),
    "c": (lambda x: x**3 - 2*x - 5,
          lambda x: 3*x**2 - 2),
    "d": (lambda x: math.exp(x) - 2,
          lambda x: math.exp(x)),
    "e": (lambda x: x - math.exp(-x),
          lambda x: 1 + math.exp(-x)),
    "f": (lambda x: x**6 - x - 1,
          lambda x: 6*x**5 - 1),
    "g": (lambda x: x**2 - math.sin(x),
          lambda x: 2*x - math.cos(x)),
    "h": (lambda x: x**3 - 2,
          lambda x: 3*x**2),
    "i": (lambda x: x + math.tan(x),
          lambda x: 1 + 1/(math.cos(x)**2)),
    "j": (lambda x: 2 - (math.log(x)/x),
          lambda x: -(1 - math.log(x))/x**2),
}

x0s = {"a":0, "b":1/4, "c":2, "d":1, "e":1, "f":1, "g":1/2, "h":1, "i":3, "j":1/3}

domain = {
    "b": lambda x: x != 0,
    "j": lambda x: x > 0,
    "i": lambda x: abs(math.cos(x)) > 1e-6,  
}

brackets = {
    "a": (0.0, 0.8),
    "b": (0.1, 0.3),
    "c": (2.0, 2.1),
    "d": (0.6, 1.0),
    "e": (0.0, 1.0),
    "f": (1.0, 1.2),
    "g": (0.5, 0.9),
    "h": (1.0, 1.4),
    "i": (1.7, 3.0),
}



for key in "abcdefghij":
    func, derivative = functions[key]
    x0 = x0s[key]
    dom = domain.get(key, lambda x: True)

    #bisection
    try:
        if key == "j":
            raise ValueError("No real root for problem j")
        a, b = brackets[key]
        bisection_root, bisection_iteration = bisection(func, a, b)
    except Exception:
        bisection_root, bisection_iteration = None, None

    #secant
    try:
        if key == "j":
            raise ValueError("No real root for problem j")
        x1 = x0 + 0.1 if dom(x0 + 0.1) else x0 - 0.1
        secant_root, secant_iteration = secant(func, x0, x1)
    except Exception:
        secant_root, secant_iteration = None, None

    #newton
    try:
        if key == "j":
            raise ValueError("No real root for problem j")
        newton_root, newton_iteration = newton_method(func, derivative, x0)
    except Exception:
        newton_root, newton_iteration = None, None

    print(key, bisection_root, bisection_iteration,
          secant_root, secant_iteration,
          newton_root, newton_iteration)
