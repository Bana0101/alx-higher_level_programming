#!/usr/bin/python3
""" module documentation """
import json


def save_to_json_file(my_obj, filename):
    """ function that reads a text file """
    with open(filename, 'w') as fd:
        json.dump(my_obj, fd)
