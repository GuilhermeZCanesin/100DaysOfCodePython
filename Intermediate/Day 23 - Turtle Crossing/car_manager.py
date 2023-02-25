import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self, s_width, s_height):
        self.all_cars = []
        self.screen_w = s_width
        self.screen_h = s_height
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        divide_screen_n = -int(self.screen_h / 2) + 50
        divide_screen_p = int(self.screen_h / 2) - 50
        x_start = self.screen_w / 2
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(divide_screen_n, divide_screen_p)
            new_car.goto(x_start, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += 5
