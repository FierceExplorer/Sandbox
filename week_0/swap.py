age1 = input("First Age: ")
age2 = input("Second Age: ")


def age_swap(first_age, second_age):
  if first_age <= second_age: 
    return first_age, second_age
  else: 
    return second_age, first_age

print(age_swap(age1, age2))