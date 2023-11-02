#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) > 2:
        print("{} arguments:".format(len(argv) - 1))
    elif len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
    else:
        print("0 arguments.")
    for x in range(1, len(argv)):
        print("{}: {}".format(x, argv[x]))

