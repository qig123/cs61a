def largest_factor(x):
    """Return the largest factor of x that is smaller than x.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    factor = x-1
    while(factor > 1):
        if(x % factor == 0):
            return factor
        factor = factor-1
    return 1


def getx():
    while(-1):
        print("5")


# print(largest_factor(2))
getx()
