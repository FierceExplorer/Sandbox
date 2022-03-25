from week_1 import InfoDb

class Fibonacci:
    def __init__(self):
        self.fiboSeq = [0, 1]
    def __call__(self, n):
        if n < len(self.fiboSeq):
            return self.fiboSeq[n]
        else:
            # Compute the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2) # two recursive calls to self (__call__(self, n))
            self.fiboSeq.append(fib_number) # builds list, with most nested of the calculations 1st... may hurt your head
        return self.fiboSeq[n]

def fib_test():
  fibo_of = Fibonacci() # object instantiation and run __init__ method
  term = int(input("Enter term for fibonacci: "))
  print(fibo_of(term)) # object running __call__ method

def combination_list(n, r):
  comb = InfoDb.recur_factorial(n) / (InfoDb.recur_factorial(r) * InfoDb.recur_factorial(n - r))
  return int(comb)


class Combination: 
  def __init__(self):
    self.comb = 1 
  def __call__(self, n, r):
    if r > n: # checks if r is less than n; r must be less than n to work 
      print("Number of choosing objects cannot be greater than total amount of objects")
    elif r == n: #  checks if r is the same as n 
      return self.comb
    else: # follows formula to calculate combination
          # uses recur_factorial made in other file 
      comb = InfoDb.recur_factorial(n) / (InfoDb.recur_factorial(r) * InfoDb.recur_factorial(n - r))
      return int(comb)

def comb_test(): 
  comb_of = Combination()
  n = int(input("Enter total number of objects: "))
  r = int(input("Enter number of choosing objects: "))
  print(comb_of(n,r))