""" Homework 1: Control """

from operator import add, sub


def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

#if statement :First c() t()/f()


def with_if_statement():
    """
    >>> result = with_if_statement()
    6
    >>> print(result)
    None
    """
    if c():
        return t()
    else:
        return f()

# if statement :First


def with_if_function():
    """
    >>> result = with_if_function()
    5
    6
    >>> print(result)
    None
    """
    return if_function(c(), t(), f())


def c():
    "*** YOUR CODE HERE ***"
    return 5 == 5


def t():
    "*** YOUR CODE HERE ***"
    print(5)


def f():
    "*** YOUR CODE HERE ***"
    print(6)


# result = with_if_statement()
# result = with_if_function()
# with_if_function()
# re = c()
# x = print(5)
# print(x)

# print(c())
# print(t())

#
# python ok -q with_if_statement --local
# python ok -q with_if_function  --local


def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    step = 1        
    while(x != 1):
        print(x)
        if(x % 2 == 0):
            x = x//2
        else:
            x = x*3+1
        step = step+1
    return step


a = hailstone(10)
print(a)
