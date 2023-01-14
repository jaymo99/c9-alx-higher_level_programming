#!/usr/bin/python3
'''
0-add_integer module.

This module defines a function that adds to integers
'''


def add_integer(a, b=98):
    ''' Returns the sum of 2 integers.

    Args:
        a: First integer
        b: Second integer
    '''
    if (type(a) is not int) and (type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int) and (type(b) is not float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return (a + b)
