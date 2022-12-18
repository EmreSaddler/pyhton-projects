from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.score = 0
        self.penup()
        self.hideturtle()
        self.setposition(-50, 275)
        self.write("Score: 0", False, align='center', font=('arial', 15, 'normal'))

    def score_add(self):
        self.score += 1
        self.write(f"Score: {self.score}", False, align='center', font=('arial', 15, 'normal'))

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", False, align='center', font=('arial', 30, 'normal'))
