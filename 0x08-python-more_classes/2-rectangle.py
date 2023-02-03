#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    Rectangle: Class that defines a rectangle
    Attributes:
    width: width of rectangle
    height: height of rectangle
    Method:
    __init__: Initializes the width and height
    """
    def __init__(self, width=0, height=0):
        """
        Args:
            width: initialize with 0
            height: initialize with 0
        """
        if (isinstance(width, int)):
            if width < 0:
                raise ValueError('width must be >= 0')
            self.__width = width
        else:
            raise TypeError('width must be an integer')

        if (isinstance(height, int)):
            if height < 0:
                raise ValueError('height must be >= 0')
            self.__height = height
        else:
            raise TypeError('height must be an integer')

    @prperty
    def width(self):
        """
           getter method
           Return:
               width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method
        Args:  value: new width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ getter method
        Return: height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method
        Args: value: new height
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        compute area of rectangle
        Return: area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        compute perimeter of rectangle
        Return:
        perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
