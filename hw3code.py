import numpy as np
import matplotlib.pyplot as plt

def divided_differences(x, y):
    n = len(x)
    coef = y.astype(float).copy()
    for j in range(1, n):
        coef[j:n] = (coef[j:n] - coef[j-1:n-1]) / (x[j:n] - x[0:n-j])
    return coef

def newton_eval(coef, xnodes, t):
    p = np.full_like(t, coef[-1], dtype=float)
    for k in range(len(coef) - 2, -1, -1):
        p = coef[k] + (t - xnodes[k]) * p
    return p

f = np.exp
t = np.linspace(-1, 1, 501)

n_values = [2, 4, 8, 16, 32]
E_values = []

for n in n_values:
    x = np.linspace(-1, 1, n + 1)   # interpolation nodes
    y = f(x)

    coef = divided_differences(x, y)
    p = newton_eval(coef, x, t)

    err = np.abs(f(t) - p)
    E_n = np.max(err)
    E_values.append(E_n)

    print(f"n = {n:2d}, E_n = {E_n:.16e}")

plt.semilogy(n_values, E_values, marker='o')
plt.xlabel('n')
plt.ylabel('E_n')
plt.title('Interpolation error for e^x on [-1,1]')
plt.grid(True)
plt.show()