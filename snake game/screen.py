import time
from turtle import Screen
from Snake import Snake

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)
snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")

game_on = True
while game_on:
    snake.move()
    time.sleep(0.1)
    screen.update()



screen.exitonclick()