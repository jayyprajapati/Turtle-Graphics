from turtle import Turtle, Screen
from randomColor import random_color, colorgram_colors

print(colorgram_colors())

color_list = [(250, 250, 249), (246, 241, 244), (222, 152, 103), (233, 237, 240), (128, 172, 199), (221, 130, 149),
              (221, 73, 90), (243, 208, 99), (17, 121, 157), (118, 176, 147), (34, 120, 82), (18, 165, 204),
              (230, 74, 70), (142, 86, 60), (116, 85, 102), (162, 209, 162), (13, 169, 120), (171, 183, 219),
              (177, 154, 75), (213, 222, 213)]

pencil = Turtle()

pencil.up()
pencil.hideturtle()
pencil.setheading(225)
pencil.forward(300)
pencil.setheading(0)
pencil.speed("fastest")

length = 1
while length < 11:
    for _ in range(10):
        pencil.down()
        pencil.dot(20, random_color())
        pencil.fillcolor()
        pencil.up()
        pencil.forward(50)
    pencil.left(90)
    pencil.forward(50)
    pencil.left(90)
    pencil.forward(500)
    pencil.right(180)
    length += 1

screen = Screen()
screen.exitonclick()
