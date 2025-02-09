from turtle import Turtle , Screen

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
  def __init__(self):
      self.segment = []
      self.create_snake()
      self.head = self.segment[0]
      self.tail = self.segment[len(self.segment)-1]

  def create_snake(self):
      coordinate = ((0,0),(-20,0),(-40,0))
      for i in coordinate:
          turtle = Turtle("square")
          turtle.penup()
          turtle.color("red")
          turtle.goto(i)
          self.segment.append(turtle)

  def move(self):
     for i in range(len(self.segment)-1 , 0, -1):
         x = self.segment[i-1].xcor()
         y = self.segment[i-1].ycor()
         self.segment[i].goto(x,y)
     self.head.forward(MOVE_DISTANCE)

  def up(self):
     if self.head.heading() != DOWN:
         self.head.setheading(UP)

  def left(self):
      if self.head.heading() != RIGHT:
          self.head.setheading(LEFT)

  def down(self):
      if self.head.heading() != UP:
          self.head.setheading(DOWN)

  def right(self):
      if self.head.heading() != LEFT:
          self.head.setheading(RIGHT)

  def addNewTurtle(self):
      turtle = Turtle("square")
      turtle.penup()
      turtle.color("red")
      x = self.segment[len(self.segment)-1].xcor()
      y = self.segment[len(self.segment)-1].ycor()
      turtle.goto(x,y - 20)
      self.segment.append(turtle)