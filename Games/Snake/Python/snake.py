import turtle
import time

width = 450
height = 400

top = height/2
bottom = -top
right = width/2
left = -right

screen = turtle.Screen()

snake = turtle.Turtle()
snake.width(5)
snake.speed(0)
snake.penup()
snake.shape("square")

def moveSnake():
  snake.forward(10)
  # snake reaches top
  if snake.ycor() > top-30:
    snake.sety(bottom+30)
  # snake reaches bottom
  if snake.ycor() < bottom+10:
    snake.sety(top-10)
  # snake reaches right
  if snake.xcor() > right-10:
    snake.setx(left+10)
  #snake reaches left
  if snake.xcor() < left+10:
    snake.setx(right-10)


def drawBorder():
  snake.goto(left, top)
  snake.pendown()
  snake.seth(0)
  snake.forward(width)
  snake.right(90)
  snake.forward(height)
  snake.right(90)
  snake.forward(width)
  snake.right(90)
  snake.forward(height)
  snake.penup()

drawBorder()
snake.goto(0,0)

def goup():
  snake.seth(90)
def goleft():
  snake.seth(180)
def godown():
  snake.seth(270)
def goright():
  snake.seth(0)

screen.listen()
screen.onkey(goup, "Up")
screen.onkey(godown, "Down")
screen.onkey(goleft, "Left")
screen.onkey(goright, "Right")

parts = []

while True:
  moveSnake()
  time.sleep(0.1)

