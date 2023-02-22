import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen_width = 800
screen_height = 800
screen = Screen()
screen.setup(screen_width, screen_height)
screen.bgcolor("black")
screen.title("PONG!")
screen.tracer(0)

LEFT_POSITION = (-(screen_width / 2) + 30, 0)
RIGHT_POSITION = ((screen_width / 2) - 30, 0)

player_left = Paddle(LEFT_POSITION, 'left')
player_right = Paddle(RIGHT_POSITION, 'right')
ball = Ball(screen_width, screen_height)
scoreboard = Scoreboard(screen_height)

screen.listen()
screen.onkey(player_right.move_up, "Up")
screen.onkey(player_right.move_down, "Down")
screen.onkey(player_left.move_up, "w")
screen.onkey(player_left.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > screen_height / 2 - 20 or ball.ycor() < -screen_height / 2 + 20:
        ball.bounce_wall()

    if ball.distance(player_right) < 45 and ball.xcor() > (screen_width / 2) - 55 \
            or ball.distance(player_left) < 45 and ball.xcor() < -(screen_width / 2) + 55:
        ball.bounce_paddle()

    if ball.xcor() > (screen_width / 2):
        ball.reset()
        scoreboard.increase_score('left')

    if ball.xcor() < -(screen_width / 2):
        ball.reset()
        scoreboard.increase_score('right')

screen.exitonclick()
