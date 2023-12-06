#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_elements = set(my_list)
    uniq_sum = 0
    for i in uniq_elements:
        uniq_sum += i
    return uniq_sum
