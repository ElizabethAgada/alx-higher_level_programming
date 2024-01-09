#!/usr/bin/python3
"""Defines a file appending function."""


def append_write(filename="", text=""):
    """Appending a string to the end of a UTF8 text file.

    Args:
        filename (str): name of file to append to.
        text (str): string to append to file.
    Returns:
        No of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as p:
        return p.write(text)
