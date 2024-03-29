#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance, or inherited instance of a class.

    Args:
        obj (any): object to check.
        a_class (type): class to match type of obj to.
    Returns:
        True - if obj is an instance or inherited instance of a-class.
        otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
