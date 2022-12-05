from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.new_level()

    def new_level(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.write(f"LEVEL: {self.level}", align="center", font=FONT)
        self.level += 1


