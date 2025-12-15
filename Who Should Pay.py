names_string = input("Enter everybody's names separated by a comma: ")
names = names_string.split(", ")
number_of_people = len(names)

import random
number = random.randint(0, number_of_people - 1)
payer = names[number]

print(f"{payer} should pay.")

