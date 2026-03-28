from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.player_define()

    def move(self):
        self.forward(MOVE_DISTANCE)  # move up by 10 pixels

    def player_define(self):
        self.penup()
        self.go_to_start()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)  # face upward

    def go_to_start(self):
        self.goto(STARTING_POSITION)  # reset to bottom center

    def turtle_complete(self):
        if self.ycor() > FINISH_LINE_Y:  # player reached the top
            return True
        else:
            return False