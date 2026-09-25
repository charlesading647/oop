# I am creating the class called Rectangle
class Rectangle:
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

    def add_height(self, amount):
        self.height = self.height + amount
        return self.height

    def add_width(self, amount):
        self.width = self.width + amount
        return self.width

rectangle1 = Rectangle(10, 15, "Blue")

print("Height", rectangle1.height)
print("Width:", rectangle1.width)
print("Color:", rectangle1.color)
print("New height:", rectangle1.add_height(5))
print("New width:", rectangle1.add_width(5))