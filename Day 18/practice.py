from turtle import Turtle as t, Screen # Documentation: https://docs.python.org/3/library/turtle.html
import random

def draw_square(tim):
    tim.shape('turtle')
    tim.color("green")
    for i in range(4):
        tim.right(90)
        tim.forward(100)


def draw_dash_lines(dash):
    dash.shape("turtle")
    dash.color('red', 'yellow')
    for i in range(50):
        dash.forward(10)
        dash.penup()
        dash.forward(10)
        dash.pendown()

def draw_angles(angles):
    angles.shape('turtle')
    angles.penup()
    angles.setposition(-100, 200)
    angles.pendown()
    print(angles.position())
    for a in range(3, 11):
        angles.color(random.choice(colours))
        for _ in range(a):
            angles.forward(100)
            angles.right(360/a)


def draw_random_walk(obj):
    direction = [0, 90, 180, 270]
    obj.speed(0)
    obj.width(15)
    for _ in range(300):
        obj.color((random.random(), random.random(), random.random()))
        obj.setheading(random.choice(direction))
        obj.forward(50)

def draw_spirograph(obj):
    obj.speed("fastest")
    for i in range(0,360,5):
        obj.color((random.random(), random.random(), random.random()))
        obj.circle(100,None,None)
        obj.setheading(i)

my_turtle = t()
draw_spirograph(my_turtle)


screen = Screen()
screen.exitonclick()