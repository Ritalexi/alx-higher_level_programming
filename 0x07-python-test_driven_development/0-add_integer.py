#!/usr/bin/python3
"""
A function that adds 2 integers a and b .
"""


def add_integer(a, b=98):
    """
    Add two integer
    Args:
    a - integer or float
    b - integer or float
    raise: - a and b must be integers or floats
     else raise type error exeption
     """


     if ((not isinstance(a, int) and not isinstance(a, float))):
         raise TypeError("a must be an integer")
     if ((not isinstance(b, int) and not isinstance(b, float))):
         raise TypeError("b must be an integer")
     return (int(a) + int(b))
