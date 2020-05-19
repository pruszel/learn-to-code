# Print the Nth Fibonnaci number recursively
def fib(n):
  if n <= 1:
    return n
  return fib(n-1) + fib(n-2)

# Ask for number
number = input("Enter a number to get a Fibonnaci number: ")
# Convert to integer
number = int(number)
# Get Fibonnaci number
result = fib(number)
# Print out number
print("Fibonnaci number",number,"is:", result)
