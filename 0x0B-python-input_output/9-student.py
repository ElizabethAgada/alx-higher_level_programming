#!/usr/bin/python3
"""Defining a class student."""


class Student:
    """Reprsenting a student."""

    def __init__(self, first_name, last_name, age):
        """Initializing a new student.

        Args:
            first_name (str): First name of the student.
            last_name (str): last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get/set a dictionary representation of the student."""
        return self.__dict__
