student_scores = {
    "Ali" : 81,
    "Rohullah" : 78,
    "Mohsen" : 99,
    "Shirin" : 74,
    "Murtaza" : 62,
    "Akbar" : 86,
}

student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)