
""" The following code is implementing the famous 'Turtle Crossing  Game'"""
import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN_TOP = 290
SLEEP = 0.1
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkeypress(fun=player.move, key="Up")
car_manager = CarManager()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(SLEEP)
    screen.update()
    car_manager.generate()
    car_manager.move()
    # Detect collision with the car
    for car in car_manager.cars:
        if player.distance(car) < 25:
            player.game_over()
            game_is_on = False
    # Detect if Player successfully went to the end of line(increase the level and reset the player and speed up the
    # car)
    if player.ycor() > SCREEN_TOP:
        player.reset_player()
        scoreboard.next_level()
        car_manager.speed_increment()

screen.exitonclick()
