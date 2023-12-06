#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in range(0, len(my_list)):
        if my_list[i] == search:
            new_element = replace
        else:
            new_element = my_list[i]
        new_list.append(new_element)
    return new_list
