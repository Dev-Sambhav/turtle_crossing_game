from turtle import Turtle, Screen
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.scoreboard_message()

    def scoreboard_message(self):
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=FONT)

    def update_scoreboard(self):
        self.score += 1
        self.scoreboard_message()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

