#!/usr/bin/python3

class Rectangle:
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('height must be an integer')
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height) * bool(self.width and self.height)

    def __str__(self):
        rect = ""
        for i in range(self.height):
            rect += str(self.print_symbol) * self.width + '\n'
        return rect[:-1]

    def __repr__(self):
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
