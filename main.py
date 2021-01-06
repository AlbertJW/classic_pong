from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random


if __name__ == '__main__':

    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    right_paddle = Paddle(350)
    left_paddle = Paddle(-350)
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()

    screen.onkey(fun=right_paddle.up, key='Up')
    screen.onkey(fun=right_paddle.down, key='Down')
    screen.onkey(fun=left_paddle.up, key='w')
    screen.onkey(fun=left_paddle.down, key='s')

    game_on = True

    while game_on:

        screen.update()
        time.sleep(ball.move_speed)

        # Detect wall collision
        if ball.ycor() > 280 or ball.ycor() <= -280:
            ball.bounce_y()
        ball.move()

        # Detect paddle collision
        d_right = ball.distance(right_paddle)
        d_left = ball.distance(left_paddle)
        if d_right < 50 and ball.xcor() > 320 or d_left < 50 and ball.xcor() < -320:
            ball.bounce_x()

        # Detect a right-side miss
        if ball.xcor() > 400:
            ball.reset()
            scoreboard.l_point()

        # Detect a left-side miss
        if ball.xcor() < -400:
            ball.reset()
            scoreboard.r_point()
            sleep_var = 0.1

    screen.exitonclick()
