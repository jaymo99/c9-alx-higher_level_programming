#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list is None:
        return None

    return list(map(lambda item: replace if search == item
                    else item, my_list))
