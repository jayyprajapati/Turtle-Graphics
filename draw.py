from turtle import Turtle, Screen

pencil = Turtle()
screen = Screen()


def go_forward():
    pencil.forward(10)


def turn_right():
    pencil.right(10)


def turn_left():
    pencil.left(10)


def go_back():
    pencil.back(10)


def clear():
    pencil.clear()
    pencil.penup()
    pencil.home()
    pencil.pendown()


screen.listen()
screen.onkey(fun=go_forward, key="w")
screen.onkey(fun=go_back, key="s")
screen.onkey(fun=turn_left, key="d")
screen.onkey(fun=turn_right, key="a")
screen.onkey(fun=clear, key="c")

screen.exitonclick()
