from turtle import Turtle

FONT = ("Courier", 10, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.goto(-290, 280)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Level {self.level}", align="left", font=FONT)

    def next_level(self):
        self.level += 1
        self.display_score()
