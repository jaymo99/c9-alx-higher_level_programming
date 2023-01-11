import json

#!/usr/bin/python3
'''Module defines JSON handling function'''


def to_json_string(my_obj):
    '''returns the JSON representation of an object(string).

    Args:
        my_obj: Object to be represented in JSON.
    Returns:
        JSON representation of an object (string)'''

    return json.dumps(my_obj)
