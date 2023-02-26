import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen_width = 600
screen_height = 600
screen = Screen()
screen.setup(screen_width, screen_height)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food(screen_width, screen_height)
scoreboard = Scoreboard(screen_height)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > ((screen_width / 2) - 15) or snake.head.xcor() < (-(screen_width / 2) + 15) \
            or snake.head.ycor() > ((screen_height / 2) - 15) or snake.head.ycor() < (-(screen_height / 2) + 15):
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
