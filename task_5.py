# Student Grade Calculator

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
    
def calculatae_three_subjects_average(sub1, sub2, sub3):
    total = sub1 + sub2 + sub3
    average = total / 3
    return average

subject_average = calculatae_three_subjects_average(float(input("Enter marks for subject 1: ")), float(input("Enter marks for subject 2: ")), float(input("Enter marks for subject 3: ")))
print(f"The average marks of the three subjects is: {subject_average}")
grade = calculate_grade(subject_average)
print(f"The student's grade based on the average is: {grade}")