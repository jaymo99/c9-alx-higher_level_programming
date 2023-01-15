#!/usr/bin/python3

'''
2-matrix_divided module.

This module provides a function that divides all elements of a matrix.
'''


def matrix_divided(matrix, div):
    '''
    Divides all elements of a matrix.

    Args:
        matrix: a list of lists of integers or floats (matrix)
        div: a divisor (int or float)

    Returns:
        a new matrix with the results.

    Example:
    >>> matrix = [
            [1, 2, 3],
            [4, 5, 6]
        ]
    >>> print(matrix_divided(matrix, 3))
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    '''
    length = 0
    new_matrix = []

    if not all(isinstance(i, list) for i in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    length = len(matrix[0])
    for sublist in matrix:
        if len(sublist) != length:
            raise TypeError("Each row of the matrix must have "
                            "the same size")

    if not all(isinstance(i, (int, float)) for sublist in matrix
               for i in sublist):
        raise TypeError("matrix must be a matrix(list of lists)"
                        " of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i, sublist in enumerate(matrix):
        new_matrix.append([])
        for j, num in enumerate(sublist):
            new_matrix[i].append(round(num / div, 2))

    return (new_matrix)
