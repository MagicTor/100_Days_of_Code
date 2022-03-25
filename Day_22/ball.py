from turtle import Turtle
from random import randint

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed(1)
        self.setheading(20)
        self.move_speed = 0.15

    def move(self):
        self.forward(self.move_speed)

    def hits_wall(self):
        return self.ycor() > 280 or self.ycor() < -280

    def reset_position(self):
        self.setposition((0, 0))
        self.move_speed = 0.15

        if randint(0, 1):
            self.setheading(randint(15, 75))
        else:
            self.setheading(randint(285, 345))
        if randint(0, 1):
            self.setheading(randint(195, 255))
        else:
            self.setheading(randint(105, 165))

    def hits_paddle(self):
        return

    #def check_collision(self):
     #   return self.xcor() < 360 or self.xcor() > -360