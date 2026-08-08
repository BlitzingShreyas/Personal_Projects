import turtle
from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        r=random.randint(125,255)
        g=random.randint(125,255)
        b=random.randint(125,255)
        turtle.colormode(255)
        self.shape("circle")
        self.penup()
        self.fillcolor((r,g,b))
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed(0)
        self.goto(random.randint(-280,280),random.randint(-280,280))

    def refresh(self):
        r = random.randint(125, 255)
        g = random.randint(125, 255)
        b = random.randint(125, 255)
        self.fillcolor((r, g, b))
        self.goto(random.randint(-280, 280), random.randint(-280, 280))