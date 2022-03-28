from random import randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(1.0, 2.0)
            car.color(COLORS[randint(0, 5)])
            car.penup()
            car.setx(300)
            car.sety(randint(-225, 250))
            self.all_cars.append(car)

    def move_cars(self, current_level=1):
        for car in self.all_cars:
            move_speed = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * (current_level-1)) # Adds speed of MOVE_INCREMENT every level
            car.backward(move_speed)
"""
    def increase_car_speed(self):
        for car in self.all_cars:
"""