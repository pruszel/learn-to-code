import random, time

# Prints out message one chunk at a time instead of all at once
def slowprint(msg): 
  index = 0
  while index < len(msg):
    r = random.randrange(4, 9)
    print(msg[index:index+r], sep='', end='', flush=True)
    index += r
    time.sleep(random.random())
  print("")
