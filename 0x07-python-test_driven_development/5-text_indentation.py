#!/usr/bin/python3
'''
Module defines one function:
    text_indentation
'''


def text_indentation(text):
    '''prints a text with 2 new lines after each of these
    characters ('.', '?', and ':').

    Args:
        text (str): text to be printed

    Raises:
        TypeError: If text is not a string
    '''

    markers = ['.', '?', ':']
    end_of_sentence = False

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        if char in markers:
            print("{}\n".format(char))
            end_of_sentence = True
        elif end_of_sentence and (char == ' ' or char == '\t'):
            continue
        else:
            print("{}".format(char), end='')
            end_of_sentence = False
