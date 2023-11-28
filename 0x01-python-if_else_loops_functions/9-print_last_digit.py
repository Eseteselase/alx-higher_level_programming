#!/usr/bin/python3
def print_last_digit(number):
    if number % 10 == 0:
        Last_digit = 0
    elif number < 0:
        Last_digit = (10 - (number % 10))
    else:
        Last_digit = number % 10
    print("{}".format(Last_digit), end="")
    return Last_digit
