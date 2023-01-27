#!/usr/bin/python3
"""a class Square that defines a square by
"""


class Square:
    """Instantiation with optional size raising exceptions
    """

    @property
    def size(self):
        """Getter that gets the integer size
        """
        return self.__size

    @size.settter
    def size(self, value):
        """Setter that sets
        """
        self.__size = value
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def __init__(self, size=0):
        """Square instantiation and rise exxcetions
        """
        self.__size = size

    def area(self):
        """Finding the area
        """
        return(self.__size * self.__size)

    def my_print(self):
        """function to print symbol
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
