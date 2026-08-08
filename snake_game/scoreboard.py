from turtle import Turtle
FONT="Verdana"
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.goto(0,270)
        self.color("white")
        self.write(arg=f"Score: {self.score}",move=False,align="center",font=(FONT,24,"normal"))
        self.hideturtle()

    def score_update(self):
        self.clear()
        self.score+=1
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=(FONT, 24, "normal"))

    def game_over(self):
        self.penup()
        self.goto(0,0 )
        self.write(arg=f"GAME OVER",move=False,align="center",font=(FONT,24,"normal"))


