#!/usr/bin/python3
"""Defines a file writing function."""


def write_file(filename="", text=""):
    """writing a string to a UTF8 text file.

    Args:
        filename (str): Name of file to write.
        text (str): text to write to file.
    Returns:
        Number of characters written.  """
    with open(filename, "v", encoding="utf8") as p:
        return p.write(text)
