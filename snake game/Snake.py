from turtle import Turtle , Screen

from oauthlib.uri_validate import segment_nz_nc

MOVE_DISTANCE = 20
class Snake:
  def __init__(self):
      self.segment = []
      self.create_snake()
      self.head = self.segment[0]

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
      self.head.setheading(90)

  def left(self):
      self.head.setheading(180)

  def down(self):
      self.head.setheading(270)

  def right(self):
      self.head.setheading(0)
