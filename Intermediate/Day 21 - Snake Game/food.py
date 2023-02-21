import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-(self.screen_width / 2) + 20, (self.screen_width / 2) - 20)
        random_y = random.randint(-(self.screen_height / 2) + 20, (self.screen_height / 2) - 20)
        self.goto(random_x, random_y)
