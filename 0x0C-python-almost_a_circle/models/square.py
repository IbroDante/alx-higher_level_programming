#!/usr/bin/python3
"""
Square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor method for Square instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Override __str__ method to return Square information
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """
        Getter method for size attribute
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update method to assign new attributes to the Square instance
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """
        Return dictionary representation of a Square instance
        """
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
