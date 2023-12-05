#!/usr/bin/python3
""" module documentation """


def read_file(filename=""):
    """ function that reads a text file """
    with open(filename, 'r') as fd:
        print(fd.read(), end="")
