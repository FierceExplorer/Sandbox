class Palindrome:     
  def __call__(self, word):
    if 1 == len(word):
      return true 
    return word == word[::-1]


def palin_test():
  palin_of = Palindrome()
  word = input("Enter word: ")
  if palin_of(word):
    print(word + " is a palindrome.")
  else:
    print(word + " is not a palindrom.")




    