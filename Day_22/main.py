from turtle import Screen
from turtle import Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle(-360)
r_paddle = Paddle(360)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()
scoreboard = Scoreboard()

"""
posl = -270
while posl < 280:
    lines = Turtle()
    lines.penup()
    lines.goto(0, posl)
    lines.pendown()
    lines.shape("square")
    lines.shapesize(1,0.25)
    lines.color("white")
    posl += 30
"""
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    if ball.hits_wall():
        ball.setheading(360-ball.heading())

    # Hits the paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.setheading(180-ball.heading()) # Reverse the direction of the ball
        ball.move_speed += 0.01
        print(ball.move_speed)

    # Scores on the left side
    if ball.xcor() < -365:
        scoreboard.r_point()
        ball.reset_position()
    # Scores on the right side
    elif ball.xcor() > 365:
        scoreboard.l_point()
        ball.reset_position()

screen.exitonclick()
