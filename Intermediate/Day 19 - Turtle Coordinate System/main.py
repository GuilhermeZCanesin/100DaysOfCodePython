import random
from turtle import Turtle, Screen


def start_turtles():
    for color in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        turtles.append(new_turtle)


def position_turtles():
    spacer = screen_height / (len(turtles) + 1)
    position = -(screen_height / 2) + spacer
    for turtle in turtles:
        turtle.penup()
        turtle.goto(x=-(screen_width / 2) + 10, y=position)
        position += spacer


turtles = []
colors = ["red", "orange", "blue", "purple", "grey", "black"]
screen_width = 500
screen_height = 400
finish_line = (screen_width / 2) - 20
is_race_on = False

screen = Screen()
screen.setup(screen_width, screen_height)
start_turtles()
position_turtles()
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > finish_line:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You`ve won! The {winning_color} was the winner!")
                is_race_on = False
            else:
                print(f"You`ve lost! The {winning_color} was the winner!")
                is_race_on = False

screen.exitonclick()
