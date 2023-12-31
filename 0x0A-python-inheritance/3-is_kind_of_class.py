#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance, or inherited instance of a class.

    Args:
        obj (any): oBJECT TO BE CHECKED.
        a_class (type): Class to match type of obj to.
    Returns:
        True - if obj is an instance or inherited instance of a-class.
        otherwise - False.
    """
    if isinstance(obj, a-class):
        return True
    return False
