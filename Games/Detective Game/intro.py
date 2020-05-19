import utils, os, time


def start():
  utils.slowprint("Hello there, what's your name?..")
  name = input()

  if name == "test":
    utils.setTestMode(True)

  time.sleep(utils.medpause)
  utils.slowprint("\n..OK, got it.")
  time.sleep(utils.bigpause)
  os.system("clear")
  time.sleep(utils.medpause)
  print("\n\n")
  utils.slowprint("Welcome, Detective "+name+"\n")
  time.sleep(utils.medpause)
  utils.slowprint("\tIt's good to have you on the team. We have a situation on our hands.\nThere is a thief on the loose, and we need your help to catch them!\n")
  time.sleep(utils.medpause)
  utils.slowprint("\tThe only evidence we have so far is a note\nthat the thief dropped at the location of their last burglery..\n")
  time.sleep(utils.medpause)
  utils.slowprint("\tWe need your help translating or deciphering the note\n so that we can figure out where the thief might go next..\n")
  time.sleep(utils.medpause)
  utils.getinput("ok", "When you're ready to continue, say 'ok'...")
  time.sleep(utils.medpause)
  utils.slowprint("\nAlright, let's get started.")
  time.sleep(utils.bigpause)
  os.system("clear")
