#!/usr/bin/python3
'''Module defines read_file function.'''


def read_file(filename=""):
    ''' reads a text file (UTF8) and prints to stdout '''

    with open(filename, encoding='utf8') as rd_file:
        print(rd_file.read())
