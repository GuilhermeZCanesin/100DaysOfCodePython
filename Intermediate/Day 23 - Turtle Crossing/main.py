import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.tracer(0)

turtle_player = Player(SCREEN_HEIGHT)
car_manager = CarManager(SCREEN_WIDTH, SCREEN_HEIGHT)
game_scoreboard = Scoreboard(SCREEN_WIDTH, SCREEN_HEIGHT)

screen.listen()
screen.onkey(turtle_player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(turtle_player) < 20:
            game_scoreboard.game_over()
            game_is_on = False

    if turtle_player.is_at_finish_line():
        turtle_player.go_to_start()
        car_manager.level_up()
        game_scoreboard.increase_score()

screen.exitonclick()
