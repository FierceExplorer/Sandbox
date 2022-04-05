# pi is equal to 22/7 because that's the numerical estimation of pi
def arclength():
    pi=22/7
    diameter = float(input('Enter the Diameter of the Circle: '))
    angle = float(input('Enter the Angle of the Circle: '))
    if angle >= 360:
        print("Not a Valid Angle")
        return
    arc_length = (pi*diameter) * (angle/360)
    print("The arclength of the circle is" , arc_length)

# The Arclength function calculates the length of an arc of a circle of a certain diameter and a certain angle measure.
def arc():
    diameter = int(input(" Choose a Number: "))
    angle = int(input(" Choose another number: "))
    arclength(diameter, angle)