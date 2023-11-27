from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        with open("scores.txt","r") as f:
            self.high_score = int(f.read())

        self.score = 0

        # self.write(f"Score : {self.score}", False, align=ALIGNMENT, font=FONT)
        self.write(f"Score : {self.score}  High Score : {self.high_score}", False, align="center", font=('Arial', 15,
                                                                                                         'normal'))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}  High Score : {self.high_score}", False, align="center", font=('Arial', 15,
                                                                                                         'normal'))

    # def game_over(self):
    #     self.home()
    #     # self.color("white")
    #     self.write(f"Game Over", False, align="center", font=('Arial', 15, 'normal'))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("scores.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.refresh()


    def refresh(self):
        self.clear()
        self.score = 0
        with open("scores.txt", mode="r") as file:
            contents = file.read()
        self.write(f"Score : {self.score}  High Score : {contents}", False, align="center", font=('Arial', 15,
                                                                                                         'normal'))


