#!/usr/bin/python
"""Defines a class Square"""
class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """initializes the square
            
        Args:
            size (int): size of a side of the square

        Return:
            None

        """
        self.size = size
        
    def area(self):
         """calculates the square's area"""
         return (self.__size ** 2)

    @property
    def size(self):
        """getter of __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
         """prints the square"""
         if self.__size == 0:
            print()
            return
         else:
            for i in range(self.__size):
                print("#" * self.__size)
