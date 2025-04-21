student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {} #creates an empy dictionary to store grades based on students' scores

for student in student_scores:
    score = student_scores[student] #checks 'key' values
    if score >= 91:
        grade = "Outstanding"
    elif score >= 81:
        grade = "Exceeds Expectations"
    elif score >= 71:
        grade = "Acceptable"
    else:
        grade = "Fail"
    
    student_grades[student] = grade

print(student_grades)