from turtle import Turtle , Screen

trle = Turtle()
trle2 = Turtle()
scrn = Screen()

trle.color("blue")
trle2.color("red")

scrn.bgcolor("orange")

def forward():
    trle.forward(100)

def rotate():
    trle.right(45)

def circle():
    trle.right(15)
    trle.forward(11)

def clear():
    trle.penup()
    trle.clear()
    trle.home()
    trle.pendown()

scrn.listen()
scrn.onkey(rotate, "r")
scrn.onkey(forward, "f")
scrn.onkey(circle, "c")
scrn.onkey(clear, "x")
scrn.exitonclick()
