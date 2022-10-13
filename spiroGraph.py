from turtle import Turtle, Screen
from randomColor import random_color

pencil = Turtle()

pencil.shape("arrow")
pencil.speed("fastest")


size = 5
for _ in range(int(360 / size)):
    pencil.color(random_color())
    pencil.circle(100)
    pencil.setheading(pencil.heading() + size)

screen = Screen()
screen.exitonclick()
