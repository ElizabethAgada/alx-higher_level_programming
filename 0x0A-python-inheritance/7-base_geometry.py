#!/usr/bin/python3
"""Defining a base geometry class BaseGeometry."""


class BaseGeometry:
    """Representing the base geometry."""

    def area(self):
        """It is not yet implemented."""
        raising Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validating a parameter as an integer.

        Args:
            name (str): Name of the parameter.
            value (int): Parameter to validate.
        Raises:
            TypeError: if the value is not an integer.
            ValueError: if the value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
