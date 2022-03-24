import math 
from week_0 import animation
from week_1 import InfoDb
from week_2 import classes, palindrome




# Creates Title 
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# List of Week 0 Stuff
week_0_func = [
    ["swap", "swap.py"], 
    ["matrix", "matrix.py"], 
    ["pyramid", "pyramid.py"],
    ["pyramid 2.0", "pyramid 2.0.py"],
    ["animations", animation.ship],
  ]

# List of Week 1 Stuff 
week_1_func = [
  ["InfoDb loops", InfoDb.InfoDb_loops],
  ["InfoDb factorial", InfoDb.InfoDb_factorial],
  ["InfoDb fibonacci", InfoDb.InfoDb_fibonacci]
]

week_2_func = [
  ["Fibonacci Class", classes.fib_test],
  ["Combination Class", classes.comb_test],
  ["Palindrome Class", palindrome.palin_test]
]

# Function for week 0 menu 
def build_week_0_():
  print()
  title = "Week 0" + banner
  buildmenu(title, week_0_func)

# Function for week 1 menu 
def build_week_1_():
  print()
  title = "Week 1" + banner
  buildmenu(title, week_1_func)

def build_week_2_():
  print()
  title = "Week 2 " + banner
  buildmenu(title, week_2_func)
# Create Weeks Menu 
week_menu =[
  ["week 0", build_week_0_],
  ["week 1", build_week_1_],
  ["week 2", build_week_2_]
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
  buildmenu(banner, week_menu)