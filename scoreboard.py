from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.lv = 1
        self.goto(-280, 260)
        self.write(arg=f"Level:{self.lv}", align="Left", font=FONT)

    def lv_up(self):
        self.lv += 1
        self.clear()
        self.write(arg=f"Level:{self.lv}", align="Left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="Center", font=("Courier", 30, "normal"))

