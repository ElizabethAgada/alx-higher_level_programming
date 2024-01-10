#!/usr/bin/python3
"""Defining a class Student."""


class Student:
    """Representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initializing a new Student.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get/set a dictionary representation of the Student.

        If attrs is a list of strings, represent only the attributes
        included in the list.

        Args:
            attrs (list): (Optional) Attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {z: getattr(self, z) for z in attrs if hasattr(self, z)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for z, v in json.items():
            setattr(self, z, v)
