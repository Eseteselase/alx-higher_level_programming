#!/usr/bin/python3
my_list = [0, 1, 2, 3, 4, 5, 6]
for i in my_list:
    if i % 2 == 0 and my_list[i] != 0:
        my_list[i] = True
    else:
        my_list[i] = False
print(my_list)
