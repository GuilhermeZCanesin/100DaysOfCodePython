from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, s_height, s_width):
        super().__init__()
        self.penup()
        self.goto(-(s_width / 2) + 30, (s_height / 2) - 50)
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
