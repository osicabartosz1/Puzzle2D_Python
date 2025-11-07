class Rectangle:
    def __init__(self, inX, inY, width, height):
        self.width = width
        self.height = height
        self.X = inX
        self.Y = inY

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"