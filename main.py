import math 
from week_0 import animation
from week_1 import InfoDb
from week_2 import classes, palindrome




# Creates Title 
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# List of Week 0 Stuff
math_func = [
    ["InfoDb factorial", InfoDb.InfoDb_factorial],
    ["InfoDb fibonacci", InfoDb.InfoDb_fibonacci],
    ["Fibonacci Class", classes.fib_test],
    ["Combination Class", classes.comb_test],
    ["Palindrome Class", palindrome.palin_test]
  ]

# List of Week 1 Stuff 
patterns_func = [
  ["swap", "week_0/swap.py"], 
  ["matrix", "week_0/matrix.py"], 
  ["pyramid", "week_0/pyramid.py"],
  ["pyramid 2.0", "week_0/pyramid 2.0.py"],
  ["animations", animation.ship],
]

misc_func = [
  ["InfoDb loops", InfoDb.InfoDb_loops],
]

# Function for week 0 menu 
def math_menu():
  print()
  title = "Math" + banner
  buildmenu(title, math_func)

# Function for week 1 menu 
def patterns_menu():
  print()
  title = "Patterns" + banner
  buildmenu(title, patterns_func)

def misc_menu():
  print()
  title = "Miscellaneous" + banner
  buildmenu(title, misc_func)
# Create Weeks Menu 
menu_list =[
  ["Math", math_menu],
  ["Patterns", patterns_menu],
  ["Miscellaneous", misc_menu]
]

def buildmenu(banner, options):
  print(banner)


  functions = {}
  functions[0] = ["Exit"] 
  for op in options:
    index = len(functions)
    functions[index] = op



  
  for key, value in functions.items():
    print(key, '->', value[0])

  



  choice = input("What function would you like: ")

  try: #try converting to integer
    #convert to number
    choice = int(choice)
    if choice == 0: #exit choice, stop loop
      return        #return means leave function
    try:  #try to run as playground function
      action = functions.get(choice)[1]
      exec(open(action).read())
    except:
      try:  #try to run as function
        action()
      except:
        print(f"Bad action: {action}")
      #end function try
    #end playground try
  except ValueError: #not a number error
    print(f"Not a number: {choice}")
  except: #traps all other errors
    print(f"Invalid choice: {choice}")

  buildmenu(banner, options)

if __name__ == "__main__": 
  buildmenu(banner, menu_list)