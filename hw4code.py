from fractions import Fraction

def to_fraction_matrix(A):
    return [[Fraction(x) for x in row] for row in A]

def to_fraction_vector(b):
    return [Fraction(x) for x in b]

def lu_factor(A):
    n = len(A)
    L = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    U = [[Fraction(0) for _ in range(n)] for _ in range(n)]

    for i in range(n):
        L[i][i] = Fraction(1)

    for j in range(n):
        # Compute U
        for i in range(j + 1):
            s = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - s

        # Compute L
        for i in range(j + 1, n):
            s = sum(L[i][k] * U[k][j] for k in range(j))
            L[i][j] = (A[i][j] - s) / U[j][j]

    return L, U

def forward_substitution(L, b):
    n = len(L)
    y = [Fraction(0) for _ in range(n)]
    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))
    return y

def backward_substitution(U, y):
    n = len(U)
    x = [Fraction(0) for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]
    return x

# Original inputs
A = [
    [14, 14, -9, 3, -5],
    [14, 52, -15, 2, -32],
    [-9, -15, 36, -5, 16],
    [3, 2, -5, 47, 49],
    [-5, -32, 16, 49, 79]
]

b = [-15, -100, 106, 329, 463]

# Convert to exact fractions
A = to_fraction_matrix(A)
b = to_fraction_vector(b)

# Solve
L, U = lu_factor(A)
y = forward_substitution(L, b)
x = backward_substitution(U, y)

print([int(val) for val in x])