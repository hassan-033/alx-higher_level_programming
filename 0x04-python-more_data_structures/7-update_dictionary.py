#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    presence = 0
    for keys in a_dictionary:
        if keys == key:
            a_dictionary[keys] = value
            presence = 1
    if presence == 0:
        a_dictionary[key] = value
    return a_dictionary
