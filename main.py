from canvas import Canvas
from shapes import Square, Rectangle

canvas_width = int(input("Enter canvas width:"))
canvas_height = int(input("Enter canvas height:"))

colors = {"black": (255, 255, 255), "white": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("What do you like to draw? Enter quit to quit. ")

    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_w = int(input("Enter the width of the rectangle: "))
        rec_h = int(input("Enter the height of the rectangle: "))
        red = int(input("How much red should the rectangle have? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))
        r1 = Rectangle(x=rec_x, y=rec_y,height=rec_h, width=rec_w,color=(red, green, blue))
        r1.draw(canvas)

    if shape_type.lower() == "square":
        sqr_x = int(input("Enter the x of the square: "))
        sqr_y = int(input("Enter the y of the square: "))
        sqr_side = int(input("Enter the side of the square: "))
        red = int(input("How much red should the rectangle have? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))
        s1 = Square(x=sqr_x, y=sqr_y, side=sqr_side, color=(red, green, blue))
        s1.draw(canvas)
    if shape_type.lower() == "quit":
        break
canvas.make('canvas.png')
