#include <iostream>

int fib(int n) 
{
  /* Declare an array to store Fibonacci numbers. */
  int f[n+2];   // 1 extra to handle case, n = 0 
  int i; 
  
  /* 0th and 1st number of the series are 0 and 1*/
  f[0] = 0; 
  f[1] = 1; 
  
  for (i = 2; i <= n; i++) 
  {
      /* Add the previous 2 numbers in the series 
         and store it */
      f[i] = f[i-1] + f[i-2];
  } 
  
  return f[n];
}

int main() {
  std::cout << "Enter a number to get Fibonacci number: ";
  int number, result;
  std::cin >> number;
  result = fib(number);
  std::cout << "Fibonnaci number " << number << " is: " << result << std::endl;
}