#!/usr/bin/python3
"""
This module defines the Square class, which inherits from the Rectangle class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance with size,
        x and y coordinates, and an optional id.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        Gets the size of the square, which is equivalent to its width.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square by updating both width and height.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the Square instance.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """
        Update attributes instance using positional and keyword arguments.
        """
        attrs = ["id", "size", "x", "y"]
        if not args or len(args) == 0:
            for i, x in kwargs.items():
                if i in attrs:
                    self.__setattr__(i, x)
            return

        self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square instance.
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
