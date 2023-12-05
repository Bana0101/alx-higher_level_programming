#!/usr/bin/python3
""" module documentation """


def is_same_class(obj, a_class):
    """ a function that returns True or false"""
    if isinstance(obj, a_class):
        return True
    return False


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
