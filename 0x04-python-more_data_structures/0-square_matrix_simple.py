#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None

    new_matrix = []

    ''' Deep copy matrix to new_matrix '''
    for i in range(len(matrix)):
        temp = []
        for item in matrix[i]:
            temp.append(item)
        new_matrix.append(temp)
    ''' ---------------------------- '''

    for row in new_matrix:
        for item in row:
            row[row.index(item)] = item ** 2

    return new_matrix
