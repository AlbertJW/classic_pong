from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.create_net()
        self.goto(-100, 210)
        self.write(self.l_score, align="center", font=("Arial", 60, "bold"))
        self.goto(100, 210)
        self.write(self.r_score, align="center", font=("Arial", 60, "bold"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def create_net(self):
        self.goto(0, -300)
        self.width(5)
        self.seth(90)
        for _ in range(0, 30):
            self.forward(10)
            self.pendown()
            self.forward(10)
            self.penup()
        self.width(1)
        self.seth(0)

