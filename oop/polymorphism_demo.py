import math
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override the area method")


class rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return f"{self.length * self.width}"
    
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(Self):
        return math.pi * self.radius**2