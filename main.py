import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

# create a Player
player = Player()
# create a car
car = CarManager()
# create the scoreboard
scoreboard = Scoreboard()

# move the player forward
screen.listen()
screen.onkey(player.move_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # create a new car on every update
    car.create_car()
    # move the car on every update
    car.move_car()

    # Detect collision with cars
    for c in car.cars_list:
        if player.distance(c) < 20:
            game_is_on = False
            scoreboard.game_over()

    # player reach the finish line
    if player.reach_finish_line():
        # update the scoreboard when player successfully reach the finish line
        scoreboard.update_scoreboard()
        # increase the car speed when score is up
        car.increase_speed()
        # reset the player position
        player.reset_position()


# exit the screen on click
screen.exitonclick()
