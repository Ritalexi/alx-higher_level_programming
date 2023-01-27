#!/usr/bin/python3
"""a class Square that defines a square by
"""


class Square:
    """Instantiation with optional size raising exceptions
    and findingbthe area
    """

    def __init__(self, size=0):
        """Square instantiation and rise exxcetions
        """
        self.__size = size

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """finding the area
        """
        return(self.__size * self.__size)
