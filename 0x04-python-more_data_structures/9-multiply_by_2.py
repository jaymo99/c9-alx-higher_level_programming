#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    return dict(list(map(lambda key: (key, a_dictionary[key] * 2),
                         a_dictionary)))
