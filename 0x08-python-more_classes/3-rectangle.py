#!/usr/bin/python3
"""
    A class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    Rectangle: defines a rectangle class
    Attributes:
    width: width of the rectangle
    height: height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        __init__: initialises constracter THE
        width and height
        Args:
        width: width of the rectangle
        height: height of the rectangle
        """
        if isinstance(width, int):
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
    else:
        raise TypeError("width must be an integer")

    if isinstance(height, int):
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
    else:
        raise TypeError("height must be an integer")

    @property
    def width(self):
        """ getter method """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method 
        Args:
        value: new width 
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        @property
        def height(self):
            """
            getter method
            Returns: height
            """
            return self.__height

        @height.setter
        def height(self, value):
            """
            setter method
            Args: value: new height
            """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

        def area(self):
            """
            method to calculate area of rectangle 
            Returns: area
            """
            return self.__width * self.__height

        def perimeter(self):
            """
            method to calculate the perimeter of a rectangle
            Returns: perimeter
            """
            if self.__width is 0 or self.__height is 0:
                return 0
            return 2 * (self.__width + self.__height)

        def __str__(self):
            """
            return string representation of a rectangle
            """
            rectangle = ""
            if self.__width is 0 or self.__height is 0:
                return rectangle
            for i in range(self.__height - 1):
                rectangle += "#" * self.__width + "\n"
            rectangle += "#" * self.__width

            return rectangle
