import numpy as np
from PIL import Image


class Square:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x : self.x + self.side, self.y : self.y + self.side] = self.color


class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x : self.x + self.height, self.y:self.y+self.width] = self.color


class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = color

    def make(self, image_path):
        img = Image.fromarray(self.data, "RGB")
        img.save(image_path)


canvas = Canvas(20, 30, (255, 255, 255))

r1 = Rectangle(1, 6, 7, 10, (100, 200, 125))
r1.draw(canvas)

s1 = Square(1, 3, 3, (0, 100, 222))
s1.draw(canvas)
canvas.make("canvas.png")


