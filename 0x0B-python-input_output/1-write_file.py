#!/usr/bin/python3
''' Module defines write_file function '''


def write_file(filename="", text=""):
    '''writes a string to a text file (UTF8).

    Args:
        filename (str): Name of the file to write to
        text (str): text string to write into the file
    Returns:
        The number of characters written.'''

    with open(filename, 'w', encoding='utf-8') as wr_file:
        return wr_file.write(text)
