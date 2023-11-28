#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number % 10 == 0:
    Last_digit = 0
elif number < 0:
    Last_digit = -(10 - (number % 10))
else:
    Last_digit = number % 10
str1 = f"Last digit of {number} is {Last_digit} and is"
if Last_digit > 5:
    print(f"{str1} greater than 5")
elif Last_digit == 0:
    print(f"{str1} 0")
elif (Last_digit < 6) & (Last_digit != 0):
    print(f"{str1} less than 6 and not 0")
