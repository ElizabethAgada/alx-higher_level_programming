#!/usr/bin/python3
"""Defines a JSON file reading function."""
import json


def load_from_json_file(filename):
    """Creates a python object from a JSON file."""
    with open(filename) as p:
        return json.load(p)
