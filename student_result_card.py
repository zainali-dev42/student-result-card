"""
Student Result Card Generator
Author: Zain Ali
Description:
    A simple Python program to generate a formatted report card
    based on student name, roll number, and marks for various subjects.
    It calculates total, average, percentage, and assigns a grade.

Technologies Used:
    - Python functions
    - User input/output
    - Conditional statements
    - Percentage, average & grade calculation
"""

# Function to get basic student information
def get_student_info():
    name = input("Enter your good name: ")
    roll_no = input("Enter your roll no.: ")
    return name, roll_no

# Function to get marks for 6 subjects
def get_marks():
    PF = int(input("Enter marks for Programming Fundamentals: "))
    EN = int(input("Enter marks for English: "))
    ICT = int(input("Enter marks for Information & Communication Technology: "))
    CVC = int(input("Enter marks for Civics: "))
    PSY = int(input("Enter marks for Psychology: "))
    ISL = int(input("Enter marks for Islamiat: "))
    return PF, EN, ICT, CVC, PSY, ISL

# Function to calculate total and average marks 
def calculate_total_average_percentage(PF, EN, ICT, CVC, PSY, ISL):
    total = PF + EN + ICT + CVC + PSY + ISL
    average = total / 6
    percentage = (total / 300) * 100
    return total, average, percentage

# Function to assign grade based on average
def assign_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else: 
        return "F"

# Function to print a nicely formatted report card
def print_result_card(name, roll_no, PF, EN, ICT, CVC, PSY, ISL, total, average, percentage, grade):
    print("\n|======STUDENT RESULT CARD======|\n")
    print("Name                                :", name)
    print("Roll no                             :", roll_no)
    print("_________________________________")
    print("Programming Fundamentals            :", PF)
    print("English                             :", EN)
    print("Information & Communication Tech    :", ICT)
    print("Civics                              :", CVC)
    print("Psychology                          :", PSY)
    print("Islamiat                            :", ISL)
    print("_________________________________")
    print("Total                               :", total)
    print("Average                             :", round(average, 2))
    print("Percentage                          :", round(percentage, 2), "%")
    print("Grade                               :", grade)
    print("|===============================|")

# ====== MAIN PROGRAM ======
name, roll_no = get_student_info()

PF, EN, ICT, CVC, PSY, ISL = get_marks()

total, average, percentage = calculate_total_average_percentage(PF, EN, ICT, CVC, PSY, ISL)

grade = assign_grade(percentage)

print_result_card(name, roll_no, PF, EN, ICT, CVC, PSY, ISL, total, average, percentage, grade)