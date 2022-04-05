import re

class Palindrome:     
  def __call__(self, word):
    str(word) # makes sure that input is string 
    new_word = (re.sub('[^a-zA-Z0-9]', '', word)).lower() # checks each value with RegEx values; removes if not lowercase or capital letters or numbers
    return new_word == new_word[::-1] # checks if reversing the string is same as normal string 


def palin_test():
  palin_of = Palindrome()
  word = input("Enter word: ")
  if palin_of(word):
    print(word + " is a palindrome.")
  elif palin_of(word) == False:
    print(word + " is not a palindrome.")
  else: # makes sure to cover all test options 
    print("Oh no! Something went wrong!")


    