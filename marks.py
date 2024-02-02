def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

num_subjects = int(input("Enter the number of subjects: "))
total_marks = 0

for i in range(num_subjects):
    marks = float(input(f"Enter the marks of subject {i+1}: "))
    total_marks += marks
average_marks = total_marks / num_subjects
grade = calculate_grade(average_marks)
print(f"Average marks: {average_marks}")
print(f"Grade: {grade}")
