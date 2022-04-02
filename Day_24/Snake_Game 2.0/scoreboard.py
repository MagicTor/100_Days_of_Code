import turtle
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 14, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.get_high_score()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_scoreboard()

    def get_high_score(self):
        with open("data.txt") as file:
            self.high_score = int(file.read())

    def save_high_score(self):
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))

#    def game_over(self):
#        self.goto(0, 0)
#        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

