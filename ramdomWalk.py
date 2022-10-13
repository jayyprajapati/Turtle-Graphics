import random
from turtle import Turtle, Screen

pencil = Turtle()
pencil.width(15)
pencil.shape("arrow")
pencil.speed("fastest")


directions = [0, 90, 180, 270]

for _ in range(200):
    pencil.color(random.random(), random.random(), random.random())
    pencil.forward(30)
    pencil.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
