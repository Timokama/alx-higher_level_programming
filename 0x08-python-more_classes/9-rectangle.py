#!/usr/bin/python3
"""Module containing Rectangle class"""

class Rectangle:
    """Class to create a rectangle

    Attributes:
        number_of_instances (int): total number of instances of Rectangle
            in existence.
        print_symbol: symbol used by __str__ method for formatting
            output for printing.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle with `width` and `height`.
        
        Args:
            width (int): width of rectangle with value >= 0.
            height (int): height of rectangle with value >= 0.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Getter function for `width` attribute.

        Returns: value of `width` attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for `width` attribute.

        Args:
            value (int): value to use for `width`.
        Raises:
            TypeError: If `value` is not of type int.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be an integer')
        self.__width = value

    @property
    def height(self):
        return self.__height
    """Getter function for `height` attribute.

    Returns: value of `height` attribute.
    """
    @height.setter
    def height(self, value):
        """Setter function for `height` attribute.

        Args:
            value (int): value to use for `height`.

        Raises:
            TypeError: If `value` is not of type int.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Method to compute area of Rectangle instance"""
        return self.width * self.height
    
    def perimeter(self):
        """Method to compute perimeter length of Rectangle instance.

        Returns: 2 * (w + h) if both `width` and `height` > 0, else 0.
        """
        return 2 * (self.width + self.height) * bool(self.width and self.height)

    def __str__(self):
        """Format Rectangle instance for printing as a grid.

        Returns: string contain `width` columns and `height` rows of
            'print_symbol`.
        """
        rect = ""
        for i in range(self.height):
            rect += str(self.print_symbol) * self.width + '\n'
        return rect[:-1]

    def __repr__(self):
        """Format Rectangle instance so that eval(self.__repr__())
        creates a new similar instance.

        Returns: string representation to recreate object.
        """
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """Method called upon deletion of instance with `del`.

        Prints a message "Bye rectangle..." when deleted. Also,
        decrements class variable `number_of_instances`.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to compare two Rectangle instances by area.

        Args:
            rect_1 (Rectangle): first instance.
            rect_2 (Rectangle): secong instance.
        Returns: The larger of the two rectangles, or `rect_1` if they
            are equal.

        Raise: TypeError: If `rect_1` or `rect_2` are not of type Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Class method to create square via the Rectangle interface.

        Args:
            size (int): side lengths of square.

        Return: new Rectangle instance with equal side lengths.
        """
        return cls(size, size)
