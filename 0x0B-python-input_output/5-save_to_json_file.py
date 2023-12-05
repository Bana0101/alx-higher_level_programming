#!/usr/bin/python3
""" module documentation """
import json


def save_to_json_file(my_obj, filename):
    """ function that reads a text file """
    with open(filename, 'w') as fd:
        json.dump(my_obj, fd)

def set_default(obj):
    """ convert a set to a list for json serialization"""
    if isinstance(obj, set):
        return list(obj)
    raise TypeError("the object is not JSON serialization")
