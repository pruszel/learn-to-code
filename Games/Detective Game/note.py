import utils, time

def clue1():
  utils.levelStart("Level 1")
  utils.slowprint("The first thing written on the note says..\n")
  utils.slowprint("\t\"Going to The Big Apple..\n\t see you in "+utils.simple_encrypt("New York")+".\"\n")
  utils.slowprint("Where do you think the thief is going next?")
  city = ""
  while city != "New York":
    city = input()
    if city.lower() == "new york":
      utils.slowprint("That right, good guess! ")
      break
    else:
      utils.slowprint("I don't think that's correct...guess again")
