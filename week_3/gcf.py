import math
# The math module above needs to be imported into the .py file in order to access the mathematical functions.


# Function to find the GCD of two Numbers
def findgcd(num1, num2):
    if num1 == 0:
        return num1
    while num2 != 0:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1

# a and b in this instance are tied to the inputs of the user and the gcd function finds the gcds of user's inputs.
def gcd():
    a = int(input(" Enter a value: "))
    b = int(input(" Pick another Number: "))
    gcd = findgcd(a, b)
    print("\n The GCF of {0} and {1} is: {2}".format(a, b, gcd))
    print()