#!/usr/bin/python3
'''
Module defines one function:
    print_square: prints a square with the character '#'
'''


def print_square(size):
    '''Prints a square with the character '#'.

    Args:
       size (int): The length of the square

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is not a positive integer
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for col in range(size):
            print("#", end='')
        print()
