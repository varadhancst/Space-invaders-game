from turtle import Turtle


class Enemy(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(270)
        self.penup()
        self.dx = 10
        self.dy = 10
        self.goto(x, y)
        self.x = 1

    def enemy_move(self):
        self.forward(5)






