from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # slow down the creation of car
        random_number = randint(1, 6)
        # new car is generated only if random number is equal to 5
        if random_number == 5:
            car = Turtle(shape="square")
            car.penup()
            car.color(choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.goto(300, randint(-250, 250))
            self.cars_list.append(car)

    def move_car(self):
        for car in self.cars_list:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
