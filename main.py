from turtle import Screen
from player import Player
from bullet import Bullet
from scoreboard import Scoreboard
from enemies import Enemy
import time
import random

screen = Screen()
screen.tracer(0)
screen.title("Space Invaders")
screen.bgcolor("black")
screen.setup(width=800, height=600)

player = Player((0, -250))

bullet = Bullet((player.xcor(), player.ycor()))
enemies = []
x_position = -360
y_position = 150
for i in range(15):
    enemy = Enemy(x_position, y_position)
    enemies.append(enemy)
    x_position += 50

screen.onkeypress(player.player_left, "Left")
screen.onkeypress(player.player_right, "Right")

lives = Scoreboard((-100, 200))
points = Scoreboard((100, 200))

game_is_on = True

while game_is_on:
    screen.listen()
    bullet.bullet_move()

    time.sleep(bullet.move_speed)
    screen.update()
    special = random.choice(enemies)
    special.enemy_move()

    if bullet.ycor() > 150:
        bullet.reset_position((player.xcor(), player.ycor()))

    for brick in enemies:
        if bullet.distance(brick) < 15:
            print(bullet.move_speed)
            bullet.reset_position((player.xcor(), player.ycor()))
            brick.hideturtle()
            enemies.remove(brick)
            points.update_points()

    if special.ycor() == -280:
        print("crossed")
        lives.update_points()
        enemies.remove(special)

    if len(enemies) == 0 or lives.points > 3:
        points.game_over()
        game_is_on = False

screen.exitonclick()
