import math

class Shape:
    def area(self):
        """
        Base method for calculating the area.
        Derived classes must override this method.
        """
        raise NotImplementedError("Subclasses must implement the 'area' method.")

class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Initializes a Rectangle with given length and width.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """
        Initializes a Circle with a given radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.
        """
        return math.pi * (self.radius ** 2)
