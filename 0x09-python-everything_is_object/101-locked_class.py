#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Preventing d user from instatialating new LocjedClass attributes
    for anything but attributes called 'firstname.'
    """

    __slots__ = ["first_name"]
