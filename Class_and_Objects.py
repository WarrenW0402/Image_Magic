# Classes Example

# Create some classes and objects
import math

class Shape:
    """Represents a 2-dimensional polygon

    Attributes:
        num_sides: An integer count of the sides
        side_length: A float of side length
    """

    def __init__(self):
        """Creates a new shape with default values."""
        self.num_sides = 4
        self.num_length = 10.0

    def area(self) -> float:
        """Return the area of a square."""
        return self.num_length ** 2

    def perimeter(self) -> float:
        """Return the perimeter of the square"""
        return self.num_sides * self.num_length

some_shape = Shape()
print(some_shape.area(), some_shape.perimeter())

class Circle(Shape):
    """Represents a circle which IS A shape

    Attributes:
        radius: A float indicating the radius
    """

    def __init__(self, radius: float = 5):
        """Creates a circle with a default radius of 5."""
        super().__init__()

        self.radius = radius
        self.num_sides = 1

    def area(self) -> float:
        """Returns the area of the circle"""
        return math.pi * self.radius

    def perimeter(self) -> float:
        """Returns the perimeter of the cirle"""
        return math.pi * 2 * self.radius

circleShape = Circle()
print(circleShape.area(), circleShape.perimeter())