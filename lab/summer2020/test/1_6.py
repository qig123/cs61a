def square(x):
    return x*x


def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total, k = total+k, k+1
    return total


def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total+k*k*k, k+1
    return total


def pi_sum(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / ((4*k-3) * (4*k-1)), k+1
    return total


def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total+term(k), k+1
    return total


def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess


def average(x, y):
    return (x+y)/2


def approx_eq(x, y, tolerance=1e-15):
    return abs(x-y) < tolerance


def sqrt(a):
    def sqrt_update(x, a):
        return average(x, a/x)

    def sqrt_close(x):
        return approx_eq(x*x, a)
    return improve(sqrt_update, sqrt_close)


def compose1(f, g):
    def h(x):
        return f(g(x))
    return h
