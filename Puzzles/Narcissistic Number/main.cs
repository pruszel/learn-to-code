//
// http://mathworld.wolfram.com/NarcissisticNumber.html
//
using System;

class MainClass
{
  public static void Main (string[] args) {
    isNarcissistic(122);
  }
  public static bool isNarcissistic(int value)
  {
    int numDigits = 1;
    int remainder = value;
    while(remainder > 10) {
      remainder = remainder/10;
      numDigits++;
    }
    
    

    return false;
  }
}