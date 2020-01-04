#
# Create an upside-down number pyramid like so..
#
#         1
#       2 1 2
#     3 2 1 2 3
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5
#

print("Enter pyramid height: ")
height = int(input())
print()

for row in range(0, int(height)):
  numSpaces = (height - (row+1)) * 3
  line = ' ' * numSpaces

  for num in range(row + 1, 0, -1):
    line = line + str(num) + "  "
  
  print(line, end='')
  line = line[0:len(line) - 5]
  print(line[::-1], end='\n')
