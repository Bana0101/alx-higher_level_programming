#!/usr/bin/python3
"""module documentation"""


def text_indentation(text):
    """  a function that prints a text with 2 new lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for x in range(len(text)):
        print(text[x], end='')
        if text[x] == '.' or text[x] == '?':
            x += 1
            print()
            print()


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
