import time
from turtle import Screen

from snake import Snake


def position_turtles():
    pass


screen_width = 600
screen_height = 600
screen = Screen()
screen.setup(screen_width, screen_height)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.3)
    snake.move()

screen.exitonclick()
