from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.write(f"Score : {self.score}", align= "center", font = ("Arial",24,"normal"))
        self.hideturtle()

    def UpdateScore(self):
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))

    def ScoreAdd(self):
        self.score += 1
        self.clear()
        self.UpdateScore()




