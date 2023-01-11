from turtle import Turtle

FONT = ('Arial', 30, 'normal')


class Scoreboard(Turtle):
    def __init__(self, goto):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(goto)
        self.lives = 0
        self.points = 0
        self.write(f"{self.lives}", font=FONT, align="center")
        self.write(f"{self.points}", font=FONT, align="center")

    def update_lives(self):
        self.lives += 1
        self.clear()
        self.write(f"{self.lives}", font=FONT, align="center")

    def update_points(self):
        self.points += 1
        self.clear()
        self.write(f"{self.points}", font=FONT, align="center")
        return self.points

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over\nYour score is: {self.points}", font=FONT, align="center")






