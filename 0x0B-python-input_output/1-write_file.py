#!/usr/bin/python3
""" module documentation """


def write_file(filename="", text=""):
    """ function that reads a text file """
    with open(filename, 'w') as fd:
        n = fd.write(text)
    return n
