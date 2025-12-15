print("Welcome to Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = (name1 + name2).lower()

first_digit = names.count("t") + names.count("r") + names.count("u") + names.count("e")
second_digit = names.count("l") + names.count("0") + names.count("v") + names.count("e")

score = int(str(first_digit) + str(second_digit))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")



