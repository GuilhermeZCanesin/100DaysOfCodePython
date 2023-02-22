from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")


class Scoreboard(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, (screen_height / 2) - 40)
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 250)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self, scorer):
        if scorer == 'left':
            self.left_score += 1
            self.update_scoreboard()
        elif scorer == 'right':
            self.right_score += 1
            self.update_scoreboard()
