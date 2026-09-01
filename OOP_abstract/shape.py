from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        pi = 3.14159
        return pi * (self.radius ** 2)


rectangle = Rectangle(5, 4)
circle = Circle(6)

shapes = [rectangle, circle]

for shape in shapes:
    print(shape.calculate_area())