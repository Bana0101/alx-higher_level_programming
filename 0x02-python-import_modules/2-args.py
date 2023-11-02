#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    for x in range(1, len(argv)):
        print("{}: {}".format(x, argv[x]))

