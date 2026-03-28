from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:  # 1 in 6 chance a new car spawns each tick
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)  # make it look like a car
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)  # spawn on the right side at a random height
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)  # move all cars to the left

    def level_up(self):
        self.car_speed += MOVE_INCREMENT  # speed up cars each level