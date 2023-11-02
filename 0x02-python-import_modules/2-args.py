#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        print("{} arguments:".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
    else:
        print("0 arguments.")
    for x in range(1, len(sys.argv)):
        print("{}: {}".format(x, sys.argv[x]))

