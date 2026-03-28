import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # turn off auto updates so we control when screen refreshes
screen.listen()

player = Player()
screen.onkey(player.move, "Up")  # move player up when Up arrow is pressed

car_manage = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)  # small delay so the game doesn't run too fast
    screen.update()
    car_manage.create_cars()
    car_manage.move_car()

    # check if any car hits the player
    for car in car_manage.all_cars:
        if car.distance(player) < 20:
            score.game_over()

    # if player reached the top, reset and go to next level
    if player.turtle_complete():
        player.go_to_start()
        car_manage.level_up()
        score.increase_score()

screen.exitonclick()