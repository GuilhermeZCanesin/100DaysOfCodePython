from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

with open("high_score.txt") as file:
    contents = file.read()
    file_high_score = int(contents)


class Scoreboard(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.score = 0
        self.high_score = file_high_score
        self.color("white")
        self.penup()
        self.goto(0, (screen_height / 2) - 40)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode='w') as overwrite:
                overwrite.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
