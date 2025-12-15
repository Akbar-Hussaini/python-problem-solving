student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

i = 0
sum = 0
for item in student_heights:
    i += 1
    sum += item

average_height = sum / i
print(f"The average height is {round(average_height)}")


# items = len(student_heights)
# sum = sum(student_heights)
# average_height = sum / items
# print(round(average_height))
