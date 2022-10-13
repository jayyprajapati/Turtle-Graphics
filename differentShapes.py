from turtle import Turtle, Screen
from randomColor import random_color

paint_brush = Turtle()
paint_brush.shape("arrow")
paint_brush.speed("fastest")

angle = 360
i = 3
while i < 11:
    paint_brush.color(random_color())
    for _ in range(i):
        paint_brush.forward(100)
        paint_brush.right(angle / i)
    i += 1

screen = Screen()
screen.exitonclick()
