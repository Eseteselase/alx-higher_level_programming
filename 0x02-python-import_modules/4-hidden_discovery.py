#!/usr/bin/python3
import sys
if __name__ == "__main__":
    import hidden_4
    for i in dir(hidden_4):
        if not i.startswith("__"):
            print("{}".format(i))
