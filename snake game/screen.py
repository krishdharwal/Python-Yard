import time
from turtle import Screen, Turtle
from Snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
snake = Snake()
food = Food()
scorecard = ScoreBoard()

screen.setup(600,600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")

score = 0
game_on = True
while game_on:
    snake.move()
    time.sleep(0.1)
    screen.update()

   # Board Edge Collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scorecard.gameOver()
        game_on = False

    # Snake Food Collision
    if snake.head.distance(food) < 20:
        score += 1
        scorecard.increaseScore()
        food.refresh()
        snake.addNewTurtle()

    # slice the list from 1
    for i in snake.segment[1:]:
        if snake.head.distance(i)  < 10:
            scorecard.gameOver()
            game_on = False

screen.exitonclick()