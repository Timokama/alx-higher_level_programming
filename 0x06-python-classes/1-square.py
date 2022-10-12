#!/usr/bin/python3
"""defines a class Square"""

class Square:
    """class defines a squara"""
    def __init__(self, size):
        """initializes the square
        
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("sizemust be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
