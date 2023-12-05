#!/usr/bin/python3
""" sys module to get the arguments"""
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
my_dict = []
try:
    my_dict.extend(load_from_json_file(filename) + list(sys.argv[1:]))
except Exception:
    my_dict.extend(list(sys.argv[1:]))

save_to_json_file(my_dict, filename)
