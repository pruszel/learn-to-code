import turtle

# Setup turtle
t = turtle.Turtle()
t.hideturtle()

s = turtle.Screen()

# X's turn = 1
# O's turn = 0
player = 1


def drawX(t):
  t.speed('normal')
  t.pendown()
  t.seth(45)
  t.forward(100)
  t.penup()
  t.backward(50)
  t.seth(135)
  t.backward(50)
  t.pendown()
  t.forward(100)

def drawO(t):
  t.speed('normal')
  t.pendown()
  t.circle(40)

def drawBoard():
  global t
  s.reset()
  t.speed('fastest')
  t.penup()
  t.goto(0,0)
  t.seth(270)
  t.pendown()
  t.forward(350)
  t.penup()
  t.goto(150, 0)
  t.pendown()
  t.forward(350)
  t.penup()
  t.goto(-100, -100)
  t.seth(0)
  t.pendown()
  t.forward(350)
  t.penup()
  t.goto(-100, -250)
  t.pendown()
  t.forward(350)
  t.speed('normal')

def click(x, y):
  t.penup()
  t.goto(x, y)
  global player
  if player == 1:
    drawX(t)
    player = 0
  else:
    drawO(t)
    player = 1

drawBoard()
s.onclick(click)

# Button to clear the screen
clear = turtle.Turtle()
clear.hideturtle()
clear.penup()
clear.goto(0, 100)
clear.write("Clear", font=("Arial", 14))
clear.onclick(drawBoard)



s.mainloop()
