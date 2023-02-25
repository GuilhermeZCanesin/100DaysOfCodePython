from turtle import Turtle

MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self, s_height):
        super().__init__()
        self.starting_position_y = (-s_height / 2) + 20
        self.finish_line = (s_height / 2) - 20
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_to_start(self):
        self.goto(0, self.starting_position_y)

    def is_at_finish_line(self):
        if self.ycor() > self.finish_line:
            return True
        else:
            return False
