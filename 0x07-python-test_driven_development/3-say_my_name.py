#!/usr/bin/python3
'''
Module defines one function:
    say_my_name - prints first name and last name
'''


def say_my_name(first_name, last_name=""):
    '''Prints a message with the name of the person.

    Args:
        first_name (str): The first name of the person.
        last_name (str, optional): The last name of the person.
            Defaults to "".

    Raises:
        TypeError: If firs_name or last_name is not a string.
    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
