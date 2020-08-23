from operator import add, mul, sub


def square(x): return x * x


def identity(x): return x


def triple(x): return 3 * x


def increment(x): return x + 1


HW_SOURCE_FILE = __file__


def product(n, term):
    """Return the product of the first n terms in a sequence.
    n -- a positive integer
    term -- a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
    product, k = 1, 1
    while k <= n:
        product, k = product*term(k), k+1
    return product


def accumulate(combiner, base, n, term):
    """Return the result of combining the first n terms in a sequence and base.
    The terms to be combined are term(1), term(2), ..., term(n).  combiner is a
    two-argument commutative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> accumulate(lambda x, y: 2 * (x + y), 2, 3, square)
    58
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    "*** YOUR CODE HERE ***"
    total, k = base, 1
    while k <= n:
        total = combiner(total, term(k))
        k = k+1
    return total


def summation_using_accumulate(n, term):
    """Returns the sum of term(1) + ... + term(n). The implementation
    uses accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> from construct_check import check
    >>> # ban iteration and recursion
    >>> check(HW_SOURCE_FILE, 'summation_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return accumulate(add, 0, n, term)


def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> from construct_check import check
    >>> # ban iteration and recursion
    >>> check(HW_SOURCE_FILE, 'product_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return accumulate(mul, 1, n, term)


def compose1(func1, func2):
    """Return a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f


def make_repeater(func, n):
    """Return the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    # Yes, it makes sense to apply the function zero times!
    >>> make_repeater(square, 0)(5)
    5
    """
    "*** YOUR CODE HERE ***"
#    return accumulate(func, (lambda x: x), n, compose1(func, func))
    if n == 0:
        return (lambda x: x)
    elif n == 1:
        return func
    else:
        k = 1
        total_f = func
        while k < n:
            total_f = compose1(func, total_f)
            k += 1
        return total_f


def make_repeater2(func, n):
    def init_f(n):
        if n == 0:
            return (lambda x: x)
        else:
            return func
    return accumulate(compose1, init_f(n), n-1, (lambda x: func))


def zero(f):
    return lambda x: x


def successor(n):
    return lambda f: lambda x: f(n(f)(x))


def one(f):
    """Church numeral 1: same as successor(zero)"""
    "*** YOUR CODE HERE ***"
    # f1=(lambda n:lambda f:lambda x: f(n(f)(x)) )(n)  n=zero
    # successor(zero)= lambda f: lambda x: f(zero(f)(x))
    return lambda x: f(x)


def two(f):
    """Church numeral 2: same as successor(successor(zero))"""
    "*** YOUR CODE HERE ***"
    # one(f)=  lambda f: lambda x:f(x)(f)=lambda x:f(x)
    # successor(one)= lambda f: lambda x: f(lambda x:f(x)(x))=lambda f: lambda x: f(f(x))
    return lambda x: f(f(x))


three = successor(two)


def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    "*** YOUR CODE HERE ***"
    return n(increment)(0)


def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> church_to_int(add_church(two, three))
    5
    """
    "*** YOUR CODE HERE ***"
    k = 0
    n_int = church_to_int(n)
    while k < n_int:
        f = successor(m)
        m = f
        k += 1
    return m


def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.

    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    "*** YOUR CODE HERE ***"
    k = 0
    n_int = church_to_int(n)
    sum = zero
    while k < n_int:
        sum = add_church(sum, m)
        k += 1
    return sum


def pow_church(m, n):
    """Return the Church numeral m ** n, for Church numerals m and n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    "*** YOUR CODE HERE ***"
    k = 0
    n_int = church_to_int(n)
    sum = one
    while k < n_int:
        sum = mul_church(sum, m)
        k += 1
    return sum


def four(f):
    """Church numeral 1: same as successor(zero)"""
    "*** YOUR CODE HERE ***"
    # successor(zero)= lambda f: lambda x: f(zero(f)(x))
    # zero(f)=(lambda x:x)
    # zero(f)(x)=x
    return lambda x: f(f(f(f(x))))


# f = make_repeater2((lambda x: x*x), 0)
# print(f(5))
# add_three = make_repeater2(increment, 3)
# print(add_three(5))
# lambda f: lambda x: f(x) ---f=(lambda x: x)
# print(zero(identity)(1))
# f = one(identity)      lambda f: lambda x: f(x)= lambda x: x
# f = four(increment)
# print(f)
# g = f(increment)
# print(g(0))
# print(church_to_int(successor(successor(successor(two)))))
# print(church_to_int(add_church(two, three)))
# print(church_to_int(mul_church(three, four)))
# print(church_to_int(pow_church(three, two)))
