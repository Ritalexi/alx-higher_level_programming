#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle.
"""


class Rectangle:
    """
    Rectangle: the Rectangle class
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        __init__: initialize thw width and height
        """
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        getter method
        """
        if (not isinstance(self.__width, int)) or isinstance(self.__width, bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @width.setter
    def width(self, width):
        """
        setter method
        """
        if not isinstance(self.__width, int) or isinstance(self.__width, bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width


    @property
    def height(self):
        """
        getter method 
        """
        if (not isinstance(self.__height, int)) or isinstance(self.__height, bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    @height.setter
    def height(self, height):
        """
        setter method
        """
        if not isinstance(self.__height, int) or isinstance(self.__height, bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """
        area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        perimeter
        """
        if self.__height == 0 or self.width == 0:
            return 0
        return (self.__height + self.width) * 2

    def __str__(self):
        """
        Return: return  string representation of rectangle
        """
        ret_str = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for idx in range(self.__height):
            ret_str += '#' * self.width
            if idx + 1 < self.__height:
                ret_str += '\n'
        return ret_str

    def __repr__(self):
        """
        __repr__: create new object
        """
        ret_str = "Rectangle(" + str(self.__width) + ","
        ret_str += str(self.__height) + ")"
        return ret_str

    def __del__(self):
        """
        __del__: deletes instance, prints "bye" message
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
