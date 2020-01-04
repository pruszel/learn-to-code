
#
# Print Fibonacci numbers using a 'while' loop
#
def fibWhileLoop(length):
  num1, num2 = 0, 1
  print(num1)
  print(num2)
  length -= 2

  while(length > 0):
    print(num1 + num2)
    temp = num1
    num1 = num2
    num2 = temp + num2
    length -= 1

#fibWhileLoop(8)


#
# Print Fibonacci numbers using a 'for' loop
#
def fibForLoop(length):
  num1, num2 = 0, 1
  print(num1)
  print(num2)
  length -= 2

  for i in range(length):
    print(num1 + num2)
    temp = num1
    num1 = num2
    num2 = temp + num2
    length -= 1

fibForLoop(8)
