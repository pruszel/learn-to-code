import hashlib

PASSWORD_FILE = "passwords.txt"


# Get list of passwords to crack
passwords = []
def load_passwords():
  global passwords

  password_file = open("passwords.txt", "r", encoding='utf-8')
  for line in password_file:
    line = line.replace("\n", "")
    passwords.append(line)
  return passwords



# Check if generated hash matches any in passwords list
def hash_matches(my_hash):
  for h in hashes:
    if myHash == h:
      return h
  return False



# Create a list of words to test if any are in hashes list
wordList = ["fun", "sun", "bat", "not", "boom"]

# Test each word in wordList
def menu():
  while True:
    print("""
      Choose an option:
        a) search for password
        b) make new passwords
    """)
    choice = input("Choose an option")
    if choice.tolower() == "a":
      inputPassword
  pass



def inputPassword():
  pw = input("Enter a password: ")
  pw = pw.encode('utf-8')

  my_hash = hashlib.md5(pw)
  my_hash = my_hash.hexdigest()

  print()
  if hash_matches(my_hash):
    print("+ found match for", pw, "("+my_hash+")", end="\n\n")
  else:
    print("X no matches for", pw, "("+my_hash+")", end="\n\n")




# 
def makePasswords():
  wordsFile = open(PASSWORD_FILE, "r", encoding="utf-8")
  hashFile = open("md5_passwords.txt", "w", encoding="utf-8")

  for line in wordsFile:
    line = line.replace("\n", "")
    myHash = hashlib.md5(line.encode('utf-8')).hexdigest()
    hashFile.write(myHash+"\n")

  wordsFile.close()
  hashFile.close()

#makeHashes()


menu()
