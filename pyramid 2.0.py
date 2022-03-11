layers = int(input("How many layers of the pyramid: "))

star = "* "
x = 1
spaceNum = layers
while x <= layers:
  print((spaceNum * " ") + star)
  star += "* "
  spaceNum -= 1
  x += 1

