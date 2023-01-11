#!/usr/bin/python3
'''From JSON string to Python Object'''

import json


def from_json_string(my_str):
    '''returns a python object from JSON string.

    Args:
        my_str: JSON string
    Returns:
        python object (python data structure)'''

    return json.loads(my_str)
