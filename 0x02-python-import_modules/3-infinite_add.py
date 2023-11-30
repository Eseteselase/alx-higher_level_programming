#!/usr/bin/python3
import sys
if __name__ == "__main__":
    size = len(sys.argv)
    add = 0
    for i in range(1, size):
        add = add + int(sys.argv[i])
    print("{}".format(add))
