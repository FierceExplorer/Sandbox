# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "VideoGame": "Super Smash Bros Ultimate",  
               "Console": ["Nintendo Switch"],  
               "Genre": "Platform Fighter",  
               "Competitive Scene?": "Yes",  
               "Length": "35 Hours",   
               "Other Games in Series": ["Smash 64", "Smash Bros Melee", "Smash 4", "Smash Wii U"]
              })  

InfoDb.append({  
               "VideoGame": "Titanfall 2",  
               "Console": ["Xbox"],  
               "Genre": "Movement FPS",  
               "Competitive Scene?": "Yes",  
               "Length": "5 Hours ",  
               "Other Games in Series": ["Titanfall 1"]
              }) 

InfoDb.append({  
               "VideoGame": "Hades",  
               "Console": ["Nintendo Switch", "Xbox", "PC"], 
               "Genre": "Hack n Slash Roguelite",  
               "Competitive Scene?": "No",  
               "Length": "90 Hours",  
               "Other Games in Series": ["N/A"]
              })  

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["VideoGame"], ":", InfoDb[n]["Genre"])  # using comma puts space between values
    print("\t", "Other Games in Series: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Other Games in Series"]))  # join allows printing a string list with separator
    print()


# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion

## hack 2a: def for_loop()
def for_loop():
  for i in range(len(InfoDb)):
    print_data(i)

## hack 2b: def while_loop(0)
def while_loop(i):
  while i < len(InfoDb):
    print_data(i)
    i += 1
  return 

## hack 2c : def recursive_loop(0)
def recursive_loop(i):
  if i < len(InfoDb):
    print_data(i)
    recursive_loop(i + 1)
  return

def InfoDb_loops():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)

def InfoDb_factorial():
    num = int(input("Enter a number for factorial: "))
    # check if the number is negative
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        print("The factorial of", num, "is", recur_factorial(num))

# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input
def build_fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return build_fibonacci(n-1) + build_fibonacci(n-2)
  
def InfoDb_fibonacci():
  terms = int(input("Enter amount of terms in fibonacci list: "))
  if terms <= 0: 
    print("Sorry, fibonacci does not exist for negative numbers") 
  else:
    print("The list: ")
    for index in range(terms):
        print(build_fibonacci(index), ", ", end="")
  print()
    


