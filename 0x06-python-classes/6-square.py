#!/usr/bin/python3
"""Module that declare class Square with a private instance attribute size:"""


class Square:
    """class Square with a private attrivute size"""

    def __init__(self, size=0, position=(0, 0)):
        """Function to validade of the size square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Function to validade of the size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Function to validade the value of size,
        in case that been different of integer and less to zero"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Function to return of the area square"""
        return self.__size * self.__size

    def my_print(self):
        """Function that print of the square with a symbol #"""
        if self.__size == 0:
            print()
        else:
            if self.__position is None or self.__position[0] == 0:
                position = 0
            else:
                position = self.__position[0]
            for j in range(self.__position[1]):
                print()
            for i in range(0, self.__size):
                for x in range(position):
                    print(end=" ")
                for i in range(0, self.__size - 1):
                    print("#", end="")
                print("#")
