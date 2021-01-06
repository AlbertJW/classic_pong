from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_coordinates):
        super().__init__()
        self.x_coordinates = x_coordinates
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(x_coordinates, 0)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
