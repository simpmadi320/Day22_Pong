from turtle import Turtle
import math

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=2, stretch_len=2, outline=None)
        self.color("white")
        self.x_pos = 0
        self.y_pos = 0
        self.angle = 330
        self.penup()

    def move(self):
        x_dis = math.sin(math.radians(self.angle)) * 1
        y_dis = math.cos(math.radians(self.angle)) * 1
        self.x_pos = self.x_pos + x_dis
        self.y_pos = self.y_pos + y_dis
        self.goto(self.x_pos, self.y_pos)

    def normalize_angle(self, angle):
        return (angle % 90 + 90) % 90

    def hits_top(self):
        relfected_angle = self.angle
        while (relfected_angle > 90):
            relfected_angle -= 90
        print(relfected_angle)

        if self.angle > 0 and self.angle < 180:
            self.angle = 180 - self.normalize_angle(self.angle)
        else:
            self.angle = 270 - self.normalize_angle(self.angle)
        self.move()
        self.move()
        self.move()

    def hits_bottom(self):
        relfected_angle = self.angle
        while (relfected_angle > 90):
            relfected_angle -= 90

        print(relfected_angle)

        if self.angle > 0 and self.angle < 180:
            self.angle = 90 - self.normalize_angle(self.angle)
        else:
            self.angle = 360 - self.normalize_angle(self.angle)
        self.move()
        self.move()
        self.move()

    def bounce_right(self):
        relfected_angle = self.angle
        while (relfected_angle > 90):
            relfected_angle -= 90

        print(relfected_angle)

        if self.angle < 90:
            self.angle = -self.normalize_angle(self.angle)
        else:
            self.angle = 180 + self.normalize_angle(self.angle)
        self.move()
        self.move()
        self.move()

    def bounce_left(self):
        relfected_angle = self.angle
        while (relfected_angle > 90):
            relfected_angle -= 90

        print(relfected_angle)

        # up/down
        if self.angle > 270:
            self.angle = self.normalize_angle(self.angle)
        else:
            self.angle = 180 - self.normalize_angle(self.angle)

        self.move()
        self.move()
        self.move()

    def reset_ball(self):
        self.goto(0, 0)
        if self.angle > 180:
            self.angle -= 180
        else:
            self.angle += 180
