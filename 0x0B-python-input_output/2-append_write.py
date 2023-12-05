#!/usr/bin/python3
""" module documentation """


def append_write(filename="", text=""):
    """ function that reads a text file """
    with open(filename, 'a') as fd:
        n = fd.write(text)
    return n
