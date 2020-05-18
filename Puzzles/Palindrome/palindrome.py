def isPalindrome(value):
  for i in range((len(value) // 2) - 1):
    if(value[i].lower() != value[len(value)-1-i].lower()):
      print("'"+value + "' is NOT palindrome")
      return
  print("'"+value + "' IS a palindrome");

isPalindrome("Anna")
isPalindrome("Civic")
isPalindrome("Kayak")
isPalindrome("Level")
isPalindrome("Madam")
isPalindrome("Mom")
isPalindrome("Noon")
isPalindrome("Racecar")
isPalindrome("Radar")
isPalindrome("Redder")
