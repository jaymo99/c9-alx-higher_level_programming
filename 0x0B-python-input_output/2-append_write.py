#!/usr/bin/python3
'''Module defines append_write function'''


def append_write(filename="", text=""):
    '''appends a string at the end of a text file (UTF8).

    Args:
        filename (str): Name of the file object
        text (str: Text string to append to file.
    Returns:
        The number of characters added.
    '''
    with open(filename, 'a', encoding='utf-8') as app_file:
        return app_file.write(text)
