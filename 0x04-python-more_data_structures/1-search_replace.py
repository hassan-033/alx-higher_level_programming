#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i, j in enumerate(my_list):
        if j == search:
            j = replace
        new_list.append(j)
    return new_list
