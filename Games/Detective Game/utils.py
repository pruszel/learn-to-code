import random, time


bigpause = 2
medpause = 1
smlpause = 0.5

# 
testmode = False

#
spacer = "---\n"

divider = "\n-------------------------------------\n"
#
padtop="\n\n\n"

#
def levelStart(level):
  print(padtop)
  print(level)
  print(spacer)


def setTestMode(onOrOff):
  global testmode
  testmode = onOrOff
  global bigpause
  bigpause = 0
  global medpause
  medpause = 0
  global smlpause
  smlpause = 0


def getinput(answer, prompt):
  userinput = ""
  while (userinput != "ok"):
    print(divider, flush=True)
    slowprint(prompt)
    userinput = input()

# Prints out message one chunk at a time instead of all at once
def slowprint(msg): 
  index = 0
  while index < len(msg):
    r = random.randrange(4, 9)
    print(msg[index:index+r], sep='', end='', flush=True)
    index += r
    if not testmode:
      time.sleep(random.random())
  print("")

def simple_encrypt(message):
  newmessage = ""
  for i in range(len(message)):
    if i%1 == 0:
      newmessage += "*"
    else:
      newmessage += message[i]
  return newmessage


def complex_encrypt(message):
  newmessage = ""
  for i in range(len(message)):
    letter = message[i]
    if letter != " ":
      number = ord(letter)
      number = number + 1
      letter = chr(number)
    newmessage = newmessage + letter
  return newmessage
