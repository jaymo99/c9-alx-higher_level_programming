#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    scores = list(map(lambda key: a_dictionary[key], a_dictionary))
    largest = scores[0]

    # determine largest score
    for i in range(len(scores)):
        if scores[i] > largest:
            largest = scores[i]

    for key in a_dictionary:
        if a_dictionary[key] == largest:
            return key

    return None
