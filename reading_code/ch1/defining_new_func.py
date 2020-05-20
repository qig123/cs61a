from operator import add, sub, mul


def square(x):
    """ get the square of x
    x -- input number
    """
    return mul(x, x)


def sum_squares(x, y):
    return add(square(x), square(y))


def g():
    return 1

# 函数也是数据


g = 2


def g(h, i):
    return h + i


# max is a funcation
# value of f is max
f = max
max = 3
result = f(2, 3, 4)


print(square(5))
print(square(add(2, 4)))
print(sum_squares(3, 4))
print(g(1, 2))
print(result)
