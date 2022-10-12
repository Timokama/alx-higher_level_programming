#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """Class to represent a square"""
    def __init__(self, size=0,position=(0, 0)):
        """Initialize a new square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the currect size of the squre."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter of __size"""
        if type(value) is not int:
            raise TypeError('size must be a number')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):
        """prints the square"""
        if self.__size is 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    @property
    def position(self):
        """getter of __position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position"""
        if type(value) is not tuple or \
            len(value) is not 2 or \
            any(map(lambda x: type(x) is not int or x < 0, value)):
                raise TypeError("position must be a tuple of 2 positive integers")

        else:
            self.__position = value

    def __str__(self):
        """String representation of a Square instance"""
        ret = ""
        if self.__size is 0:
            return ret
        
        else:
            ret = "\n" * self.__position[1]
            for i in range(self.__size):
                ret += " " * self.__position[0]
                ret += "#" * self.__size
                ret += "\n" if i < self.__size - 1 else ""
        return ret
