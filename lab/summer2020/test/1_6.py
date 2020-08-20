def square(x):
    return x * x


def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k+1
    return total


def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k * k*k, k+1
    return total


def pi_sum(n):
    total, k = 0, 1
    while k <= n:
        total, k = total+8/((4*k-3)*(4*k-1)), k+1
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


def golden_update(guess):
    return 1/guess+1


def square_close_to_successor(guess):
    return approx_eq(guess*guess, guess+1)


def approx_eq(x, y, tolerance=1e-15):
    return abs(x-y) < tolerance


print(improve(golden_update, square_close_to_successor))


# print(square(5))
