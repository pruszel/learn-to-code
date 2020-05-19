# Assign a letter grade for the following students
#
#   A - 90 to 100
#   B - 80 to 90
#   C - 70 to 80

students = {
  "Tom": 95,
  "Joe": 79,
  "Billy": 88,
  "Andrew": 81,
  "David": 73,
  "Marcus": 90,
  "Adam": 85
}

for i in students:
  if (students[i] >= 90):
    print(i + " got an A")
  elif (students[i] >= 80):
    print(i + " got a B")
  elif (students[i] >= 70):
    print(i + " got a C")
  elif (students[i] >= 60):
    print(i + " got a D")
  else:
    print(i + " got an F")
