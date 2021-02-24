from turtle import Turtle
from random import choice, randint

X_POSITION = 250
FROM = -250
TO = 250
WEST = 180
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def generate(self):
        random_interval = randint(1, 6)
        if random_interval == 1:
            new_car = Turtle(shape='square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.setheading(WEST)
            new_car.penup()
            y_position = randint(FROM, TO)
            new_car.goto(300, y_position)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.fd(self.speed)

    def speed_increment(self):
        self.speed += MOVE_INCREMENT
