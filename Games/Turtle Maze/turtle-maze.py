import turtle

mazeWidth=150

def drawMaze():
  screen = turtle.Screen()
  screen.tracer(0)

  myMaze = turtle.Turtle()
  myMaze.width(5)
  myMaze.hideturtle()
  myMaze.speed(0)

  myMaze.penup()
  myMaze.goto(-mazeWidth,190)

  for color in ["#FF0000","#0000FF","#00FF00"]:
    drawMazeSection(myMaze, color)

  screen.tracer(1)

def drawMazeSection(myMaze, color):
  myMaze.color(color)
  myMaze.pendown()
  myMaze.forward(mazeWidth)
  myMaze.penup()
  myMaze.forward(40)
  myMaze.pendown()
  myMaze.forward(mazeWidth)
  myMaze.right(90)
  myMaze.forward(100)
  myMaze.right(90)
  myMaze.forward(mazeWidth)
  myMaze.penup()
  myMaze.forward(40)
  myMaze.pendown()
  myMaze.forward(mazeWidth)
  myMaze.right(90)
  myMaze.forward(100)
  myMaze.right(90)
  x,y = myMaze.pos()
  myMaze.penup()  
  myMaze.goto(x, y-50)
  myMaze.pendown()
  myMaze.forward(30)
  myMaze.penup()
  myMaze.forward(40)
  myMaze.pendown()
  myMaze.forward(200)
  myMaze.penup()
  myMaze.forward(40)
  myMaze.pendown()
  myMaze.forward(30)
  myMaze.penup()
  myMaze.goto(x,y-110)

drawMaze()

fred = turtle.Turtle()
fred.shape("turtle")
fred.color("magenta")
fred.width(5)
fred.penup()
fred.setheading(90)
fred.goto(mazeWidth/2-55, -160)
fred.pendown()



# Start of maze
