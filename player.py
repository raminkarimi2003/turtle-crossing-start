from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
HEADING = 90

screen = Screen()


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(HEADING)
        self.reset_player()

    def move(self):
        self.fd(MOVE_DISTANCE)

    def reset_player(self):
        self.goto(STARTING_POSITION)

    def game_over(self):
        self.hideturtle()
        screen.update()
        self.home()
        self.write("Game Over", align="center", font=("Arial", 20, "normal"))
