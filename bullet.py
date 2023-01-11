import random
from turtle import Turtle


class Bullet(Turtle):
    def __init__(self, x):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setheading(90)
        self.penup()
        self.goto(x)
        self.dx = 10
        self.dy = 10
        self.x = 1
        self.move_speed = 0.1

    def bullet_move(self):
        self.forward(5)

    def enemy_bullet_move(self):
        self.backward(5)

    def reset_position(self, x):
        self.goto(x)
        self.move_speed *= 0.9


