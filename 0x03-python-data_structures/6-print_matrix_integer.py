#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print()

    for row in matrix:
        if len(row) == 0:
            print()
        else:
            for element in row:
                print("{:d}".format(element), end='')
                if element is not row[len(row) - 1]:
                    print(" ", end='')
                else:
                    print("")
