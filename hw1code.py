import math


def newton_method(f, df, x0, tolerance = 1e-6, max_iter = 1000):
    for i in range(max_iter):
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tolerance:
            return x1, i + 1
        x0 = x1
    return x0, max_iter

def secant(f, x0, x1, tolerance = 1e-6, max_iter = 1000):
    for i in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x2 - x1) < tolerance:
            return x2, i + 1
        x0, x1 = x1, x2
    return x1, max_iter

def bisection(f, a, b, tolerance = 1e-6, max_iter = 1000):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    for i in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tolerance or (b - a) / 2 < tolerance:
            return c, i + 1
        if f(a) * f(c) < 0:
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

domain_ok = {
    "b": lambda x: x != 0,
    "j": lambda x: x > 0,
    "i": lambda x: abs(math.cos(x)) > 1e-6,  
}


for k in "abcdefghij":
    f, df = functions[k]
    x0 = x0s[k]
    ok = domain_ok.get(k, lambda x: True)

    try:
        rb, itb = bisection(f, x0, ok)
    except Exception:
        rb, itb = None, None

    try:
        x1 = None
        if k in ["b","j"]:
            x1 = x0 * 0.9 if x0 > 0 else x0 + 0.1
        if k == "i":
            x1 = x0 + 0.1
        rs, its = secant(f, x0, x1)
    except Exception:
        rs, its = None, None

    try:
        rn, itn = newton_method(f, df, x0)
    except Exception:
        rn, itn = None, None

    print(k, rb, itb, rs, its, rn, itn)
