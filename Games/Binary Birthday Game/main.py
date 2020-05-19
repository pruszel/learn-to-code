import time
import utils

# The birthday is calculated using binary numbers
#
# In each group of dates, there is a binary number in the top left corner.
# Binary numbers are powers of two: 1, 2, 4, 8, 16, ...
#
# The rest of the numbers can all be written in binary using
# the number in the top left corner.
#
# Here is an example of how to make the number 11 in binary:
#
# powers of two:        16  8   4   2   1
#                       -----------------
# binary #s to get 11:  0   1   0   1   1  =  8 + 2 + 1  = 11
#
# If you look at the dates with '8', '2', and '1' in the top left corner
# ...you will find '11' in all of them!

birthday = 0
dates = [
  """
  1   3   5   7
  9   11  13  15
  17  19  21  23
  25  27  29  31
  """,
  """
  2   3   6   7
  10  11  14  15
  18  19  22  23
  26  27  30  31
  """,
  """
  4   5   6   7
  12  13  14  15
  20  21  22  23
  28  29  30  31
  """,
  """
  8   9   10  11
  12  13  14  15
  24  25  26  27
  28  29  30  31
  """,
  """
  16  17  18  19
  20  21  22  23
  24  25  26  27
  28  29  30  31
  """
]


# Introduction
utils.slowprint("Welcome to the Birthday Guessing Game!\n")
time.sleep(2)
utils.slowprint("I bet I can guess your birthday by asking you just 5 simple questions...\n")
time.sleep(1)

# Ask 5 questions
for i in range(len(dates)):

  # Keep asking for user input until they give a 'yes' or 'no'
  userinput = ""
  while len(userinput) < 1:

    # Print out question and dates
    time.sleep(1)
    utils.slowprint("#"+str(i+1)+" is your birthday on any of the following days?")
    time.sleep(.7)
    print(dates[i])
    time.sleep(.3)

    # Ask for input and check if it matches 'yes' or 'no'
    userinput = input("type 'yes' or 'no': ")
    time.sleep(.3)
    yes = len(userinput) > 0 and userinput[0].lower() == "y"
    no = len(userinput) > 0 and userinput[0].lower() == "n"
    
    # Add binary number to birthday calculation
    if yes:
      birthday += pow(2, i)

    # Print out "thinking" dots
    time.sleep(.2)
    print(".", end='', flush=True)
    time.sleep(.3)
    print(".", end='', flush=True)
    time.sleep(.4)
    print(".", end='', flush=True)
    time.sleep(.2)

    # Print out response to input
    if yes or no:
      print("OK\n")
    else:
      utils.slowprint("Sorry, I didn't understand you. Let me ask again.\n")
      continue

# Pause and "think"
time.sleep(1)
utils.slowprint("Hmmm...")
time.sleep(3)

# Check birthday is valid
if birthday == 0:
  utils.slowprint("You answered 'no' to every question..\nbut that's not possible, it had to be one of those days. Try again and pay close attention to the numbers.")
  time.sleep(1)
  exit()

# Print out birthday
utils.slowprint("I know!")
time.sleep(1)
answer = "\nYour birthday is on the "+str(birthday)

# Apply the correct date ending i.e. 1st, 2nd, 3rd
if birthday >= 11 and birthday <= 13:
  answer += "th!"
elif birthday % 10 == 1:
  answer += "st!"
elif birthday % 10 == 2:
  answer += "nd!"
elif birthday % 10 == 3:
  answer += "rd!"
else:
  answer += "th!"
utils.slowprint(answer)
time.sleep(5)

# Print out final message
utils.slowprint("\n\nThanks for playing! Enjoy your birthday!")
print("""
       , , , , , ,
       |_|_|_|_|_|
      |~=,=,=,=,=~|
      |~~~~~~~~~~~|
    |~=,=,=,=,=,=,=~|
    |~~~~~~~~~~~~~~~|
  |~=,=,=,=,=,=,=,=,=~|
  |~~~~~~~~~~~~~~~~~~~|
(^^^^^^^^^^^^^^^^^^^^^^^)
 `'-------------------'`  
""")
