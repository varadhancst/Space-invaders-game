from turtle import Turtle


class Player(Turtle):
    def __init__(self, x):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(x)

    def player_right(self):
        x = self.xcor()
        x += 20
        self.setx(x)

    def player_left(self):
        x = self.xcor()
        x -= 20
        self.setx(x)


