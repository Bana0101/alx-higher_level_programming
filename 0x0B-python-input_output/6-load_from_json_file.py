#!/usr/bin/python3
""" module documentation """
import json


def load_from_json_file(filename):
    """ function that reads a text file """
    with open(filename, 'r') as fd:
        return json.load(fd)
