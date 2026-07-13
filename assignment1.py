# Assignment 1 : Employee bonus eligibility system
# Taking input

employee_name = input("Enter Employee Name: ")
salary = float(input("Enter Salary: "))
experience = float(input("Enter years of experience: "))
performance = float(input("Enter performance rating: "))

# Display Employee Details
print("\n----- Employee Details -----")
print("Employee Name:", employee_name)
print("Salary:", salary)
print("Experience:", experience)
print("Performance:", performance)

# Checking bonus eligibility
if salary < 50000 and experience >= 2 and performance >= 4:
    print("\nEligible for Performance Bonus!")
else:
    print("\nNot Eligible.")
    print("Reason:")

    if salary >= 50000:
        print("- Salary is 50,000 or more.")
    
    if experience < 2:
        print("-Experience is less than 2 years.")

    if performance < 4:
        print("-Performance rating is below 4.")    