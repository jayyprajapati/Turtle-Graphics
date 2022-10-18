from turtle import Turtle, Screen
import random

race_on_going = False
screen = Screen()
screen.setup(width=600, height=600)
user_input = screen.textinput(title="Turtle Race bet", prompt="Who will win the race? Enter the color: ")
if user_input:
    race_on_going = True

colors = ["red", "orange", "green", "blue", "purple"]
y_pos = [-120, -60, 0, 60, 120]

turtles = []
for i in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-280, y=y_pos[i])
    turtles.append(new_turtle)

while race_on_going:

    for turtle in turtles:
        if turtle.xcor() > 280:
            race_on_going = False
            winner = turtle.pencolor()
            if user_input == winner:
                print(f"You've Win! The winner turtle is {winner}")
            else:
                print(f"You've lost! The winner turtle is {winner}")

        rand_num = random.randint(0, 10)
        turtle.forward(rand_num)

screen.exitonclick()
