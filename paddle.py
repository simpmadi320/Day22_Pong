from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.left(90)
        self.shapesize(stretch_wid=2, stretch_len=10, outline=None)

    def up(self):
        if self.ycor() < 400:
            self.forward(10)

    def down(self):
        if self.ycor() > -400:
            self.backward(10)
