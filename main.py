from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)

leftPaddle = Paddle()
leftPaddle.goto(-420, 0)

rightPaddle = Paddle()
rightPaddle.goto(420, 0)

ball = Ball()

screen.listen()

screen.onkey(leftPaddle.up, "w")
screen.onkey(leftPaddle.down, "s")
screen.onkey(rightPaddle.up, "Up")
screen.onkey(rightPaddle.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.001)
    ball.move()

    if ball.y_pos > 380:
        ball.hits_top()
    elif ball.y_pos < -380:
        ball.hits_bottom()

    if ball.distance(leftPaddle) < 50 and ball.xcor() < -340:
        ball.bounce_left()
    elif ball.distance(rightPaddle) < 50 and ball.xcor() > 340:
        ball.bounce_right()

    if ball.x_pos < -550:
        ball.reset_ball()
    elif ball.x_pos > 550:
        ball.reset_ball()

    screen.update()

screen.exitonclick()

