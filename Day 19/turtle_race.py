import random
from turtle import Turtle, Screen
import random

FINISH_LINE = 225
COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]


def begin_race(racers):
    """Runs the race and returns the winners colour"""
    while True:
        for i in range(len(racers)):
            pace = random.randint(1,10)
            racers[i].forward(pace)
            if racers[i].xcor() > FINISH_LINE:
                return racers[i].pencolor()


def race_start_positions(racers):
    for i, y in enumerate(range(-100, 101, 40)):
        racers[i].penup()
        racers[i].setposition(-200, y)


def create_turtle(colour):
    turtle = Turtle(shape="turtle")
    turtle.color(colour)
    return turtle


screen = Screen()
screen.setup(width=500,height=400)
guess = screen.textinput("Make your bet", "Who will win the race? Enter a colour:").title()

turtles = []
for i in range(6):
    turtles.append(create_turtle(COLOURS[i]))

race_start_positions(turtles)
winner = begin_race(turtles).title()

if guess == winner:
    print(f"{winner} won! You win!")
else:
    print(f"You lose. {winner} won.")

screen.exitonclick()