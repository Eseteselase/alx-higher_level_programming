#!/usr/bin/python3
import sys

def print_art():
    art_quote = "and that piece of art is useful - Dora Korpar, 2015-10-19"
    sys.stderr.write(art_quote + "\n")
    sys.exit(1)

if __name__ == "__main__":
    print_art()
