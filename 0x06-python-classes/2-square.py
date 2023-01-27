#!/usr/bin/python3
"""a class Square that defines a square by
"""

class Square:
    """Instantiin with optional size raising exceptions
    """
    def __init__(self, size=0):
        """Square instantiation and rise exxcetions
        """
        self.__size = size

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
