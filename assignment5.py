# Assignment 5: Student Grade Analyzer

student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")

mark1 = float(input("Enter marks in Subject 1: "))
mark2 = float(input("Enter marks in Subject 2: "))
mark3 = float(input("Enter marks in Subject 3: "))
mark4 = float(input("Enter marks in Subject 4: "))
mark5 = float(input("Enter marks in Subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
percentage = total / 5

# Grade Calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

# Pass/Fail
if percentage >= 40:
    result = "Pass"
else:
    result = "Fail"

# Report Card
print("\n========== REPORT CARD ==========")
print("Student Name :", student_name)
print("Roll Number  :", roll_number)
print("Total Marks  :", total)
print("Percentage   :", percentage, "%")
print("Grade        :", grade)
print("Result       :", result)
print("=================================")