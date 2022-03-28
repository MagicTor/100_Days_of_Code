from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.penup()
        self.setposition(-280, 260)
        self.level += 1
        self.write(arg=f"Level : {self.level}", move=True, align='left', font="Courier")

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over", move=False, align='center', font="Courier")