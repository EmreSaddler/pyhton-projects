from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5, 0.5)
        self.color('red')
        self.penup()
        self.refresh()

    def refresh(self):
        new_x = random.randint(-250, 250)
        new_y = random.randint(-250, 250)
        self.setposition(new_x, new_y)
