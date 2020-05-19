import turtle, time, random

#
screen = turtle.Screen()
screen.listen()
screen.bgcolor("#7FDBFF")


#
gamewidth = 400
gameheight = 300

#
right = gamewidth/2
left = -right
top = gameheight/2
bottom = -top

#
gravity = -0.25


#
debug = turtle.Turtle()
debug.penup()
debug.ht()
debug.goto(left + 20, top - 20)

#
flappy = turtle.Turtle()
flappy.shape("turtle")
flappy.color("green")
flappy.penup()
flappy.speed(0)
flappy.setx(left+100)
flappy.dy = 0

def jump():
  if flappy.ycor() < top - 25:
    flappy.dy = 6
    #flappy.sety(flappy.ycor() + 20)
screen.onkey(jump, "Space")

def drawScreen():
  border = turtle.Turtle()
  border.color("#001f3f")
  border.speed(0)
  border.ht()
  border.penup()
  border.goto(left, top)
  border.pendown()
  border.forward(gamewidth)
  border.right(90)
  border.penup()
  border.forward(gameheight)
  border.right(90)
  border.pendown()
  border.forward(gamewidth)
  border.right(90)
  border.penup()
  border.forward(gameheight)

obstaclePos = right
obstacleWidth = 30
obstacleGap = random.randrange(bottom + 50, top - 50)

obtop = turtle.Turtle()
obtop.speed(0);
obtop.shape("square")
obtop.color("#B10DC9")
obtop.penup()
obtop.width(20)
#obtop.ht()

obbot = obtop.clone()

def drawObstacles():
  print("gap at", obstacleGap)
  print("going down", top - obstacleGap)
  print("going up", obstacleGap - bottom)
  obtop.clear()
  obbot.clear()
  
  obtop.goto(obstaclePos, top - 10)
  obtop.seth(270)
  obtop.pendown()
  obtop.forward(top - obstacleGap - 50)
  # obtop.right(90)
  # obtop.forward(obstacleWidth)
  # obtop.right(90)
  # obtop.forward(top - obstacleGap)
  
  obbot.goto(obstaclePos, bottom + 10)
  obbot.seth(90)
  obbot.pendown()
  obbot.forward(obstacleGap - bottom - 50)
  # obbot.left(90)
  # obbot.forward(obstacleWidth)
  # obbot.left(90)
  # obbot.forward(bottom + obstacleGap)

def moveObstacle():
  global obstaclePos
  global obstacleGap
  obstaclePos -= 5
  if obstaclePos <= left:
    obstaclePos = right;
    obstacleGap = random.randrange(bottom + 50, top - 50)

def rungravity():
  if flappy.ycor() >= bottom + 10:
    flappy.dy += gravity

def moveflappy():
  if flappy.dy < 0 and flappy.ycor() < bottom + 15:
    flappy.dy = 0
  if flappy.ycor() > top - 15:
    flappy.dy = gravity
  flappy.sety(flappy.ycor() + flappy.dy)


# Start the game!
drawScreen()

drawObstacles()
while True:
  rungravity()
  moveflappy()
  moveObstacle()
  drawObstacles()
  screen.update()
