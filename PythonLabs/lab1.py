from math import log, exp


def f(x):
    return x ** 2


def calculate_k(x, q):
    mult = abs(x * q)
    border = 10
    if mult > border:
        return log(abs(x2) + abs(q))
    elif mult < border:
        return exp(x2 + q)
    elif mult == border:
        return x2 + q


x, q = map(int, input("Enter the value of x and q: ").split())
x2 = f(x)
print(calculate_k(x, q))