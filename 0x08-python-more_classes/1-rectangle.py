#!/usr/bin/python3
"""class Rectangle that defines a rectangle """
class Rectangle:
    """Class to create a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle with `width` and `height`.
        Args:
            width (int): width of rectangle width value >= 0.
            height (int): height of rectanglewidth value >= 0.
        """
        self.width = width 
        self.height = height

    @property
    def height(self):
        """Getter function for 'height' attribute.

            Returns: value of 'height' attribute.
        """
        return self.__height
    @height.setter
    def height(self, value):
        """Setter function for 'height' attribute.

        Args:
            value (int): value to use for 'height'.

        Raises:
            TypeError: If `value` is not of type int.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """Getter function for 'width' attribute.

        Return:
            value of 'width' attribute.
        """
        return self.__width
    @width.setter
    def width(self, value):
        """
        Setter function for 'weight' attribute.

        Args:
            value (int): value to use for 'weight'.

        Raises:
            TypeError: If `value` is not of type int.
            ValueError: If `value` is less than 0
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__weight = value
