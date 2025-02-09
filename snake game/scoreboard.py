from turtle import Turtle

class ScoreBoard(Turtle):
     def __init__(self):
         super().__init__()
         self.penup()
         self.score = 0
         self.color("white")
         self.hideturtle()
         self.goto(0, 270)
         self.write(f"Score = {self.score}", align="center", font=("Arial",20,"normal"))

     def increaseScore(self):
         self.score += 1
         self.clear()
         self.write(f"Score = {self.score}", align="center", font=("Arial",20,"normal"))

     def gameOver(self):
         self.clear()
         self.goto(0,0)
         self.write(f" GAME OVER \n Score = {self.score}", align="center", font=("Arial",20,"normal"))


