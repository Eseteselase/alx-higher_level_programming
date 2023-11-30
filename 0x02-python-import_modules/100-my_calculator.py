#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    size = len(sys.argv)
    if size != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    opr = sys.argv[2]
    b = int(sys.argv[3])
    if opr == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif opr == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif opr == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif opr == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
