print("Welcome to BMI calculator")
weight = float(input("First, please enter your weight in Kilograms: "))
height = float(input("Please enter your height in meters: "))
bmi = round(weight / (height * height))

if bmi < 18.5:
    state = "underweight"
elif bmi < 25:
    state = "normal weight"
elif bmi < 30:
    state = "overweight"
elif bmi < 35:
    state = "obese"
else:
    state = "clinically obese"

print(f"Your BMI is {bmi}, and you are {state}.")
