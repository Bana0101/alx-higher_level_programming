#!/usr/bin/python3
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
try:
    my_dict = load_from_json_file(filename) + list(sys.argv[1:])
except Exception:
    my_dict = list(ys.argv[1:])

save_to_json_file(my_dict, filename)
