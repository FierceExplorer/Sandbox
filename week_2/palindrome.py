import re

class Palindrome:     
  def __call__(self, word):
    str(word)
    new_word = (re.sub('[^a-zA-Z0-9]', '', word)).lower()
    return new_word == new_word[::-1]


def palin_test():
  palin_of = Palindrome()
  word = input("Enter word: ")
  if palin_of(word):
    print(word + " is a palindrome.")
  elif palin_of(word) == False:
    print(word + " is not a palindrome.")
  else:
    print("Oh no! Something went wrong!")


    