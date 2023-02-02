#!/usr/bin/python3
"""
A function that prints a square with the
character #.
"""


def print_square(size):
    """
    Print a square with the # character.
    size - int 
    If size is not an integer type error and 
    if size is < 0 value error 
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
