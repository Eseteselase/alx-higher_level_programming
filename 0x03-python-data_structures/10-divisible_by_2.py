#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list == []:
        return None
    else:
        for i in my_list:
            if i % 2 == 0 and my_list[i] != 0:
                my_list[i] = True
            else:
                my_list[i] = False
        return my_list
