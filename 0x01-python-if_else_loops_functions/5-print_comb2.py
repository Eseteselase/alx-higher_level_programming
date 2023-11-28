#!/usr/bin/python3
for num in range(0, 100):
    if num == 0:
        str1 = ""
    else:
        str1 = ", "
    print("{}{:02d}".format(str1,num), end="")
print()
