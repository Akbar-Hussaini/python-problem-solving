year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            state = "Leap year"
        else:
            state = "Not leap year"
    else:
        state = "Leap year"
else:
    state = "Not leap year"

print(state)