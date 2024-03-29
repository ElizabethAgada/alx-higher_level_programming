#!/usr/bin/python3
"""Defines a text file reading function."""


def read_file(filename=""):
    """Prints contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as p:
        print(p.read(), end="")
