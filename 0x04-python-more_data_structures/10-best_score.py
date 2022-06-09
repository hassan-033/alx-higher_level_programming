#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    value_max = max(a_dictionary.values())
    for i in a_dictionary:
        if a_dictionary[i] == value_max:
            key_max = i
    return key_max
