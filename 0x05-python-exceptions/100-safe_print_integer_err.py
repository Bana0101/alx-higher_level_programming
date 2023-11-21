#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as a:
        import sys
        print(f"Exception: {a}", file=sys.stderr)
        return False
