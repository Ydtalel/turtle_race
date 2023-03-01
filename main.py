import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt='Which turtle will win the race? Enter a color: "red", '
                                                          '"orange", "yellow", "green", "blue", "purple"')
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
x = -230
y = -150

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i - 1])
    new_turtle.goto(x=x, y=y)
    y += 60
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
