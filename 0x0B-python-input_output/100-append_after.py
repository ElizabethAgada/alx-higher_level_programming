#!/usr/bin/python3
"""Defining a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserting text after each line containing a given string in a file.
    Args:
        filename (str): Name of file.
        search_string (str): String to search for.
        new_string (str): String to insert.
    """
    text = ""
    with open(filename) as o:
        for line in o:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as m:
        m.write(text)
