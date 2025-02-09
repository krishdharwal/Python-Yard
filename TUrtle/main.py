from turtle import Screen , Turtle

turtle = Turtle()
turtle.shape("turtle")
turtle.color("orange")

screen = Screen()

screen.bgcolor("green")
# screen.turtles()

def drawShape(num):
    angle = 360 / num
    for _ in range(num):
        turtle.forward(100)
        turtle.right(angle)



for i in range(3,11):
    pass

drawShape(4)

# drawShape(3)

screen.exitonclick()
