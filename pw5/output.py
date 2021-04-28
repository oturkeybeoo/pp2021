import domain
from input import *

def options():
    print("""What do yo want to do?:
    0 No I want to exit
    1 List students.
    2 List courses.
    3 Add student to the study group.
    4 Add course to study.
    5 Add student to course.
    6 Mark student in the course.
    
--------------------------------------------
    """)
    option = int(input())
    return option

def StudentMarkManagement():
    print("Welcome to Student Management Program!")
    while True:
        print("--------------------------------------------")
        for student in AllStudents:
            calculateGPA(student)
        option = options()
        if option == 0:
            compressFile()
            break
        if option == 1:
            display(AllStudents)
        elif option == 2:
            display(AllCourses)
        elif option == 3:
            addStudents()
        elif option == 4:
            addCourses()
        elif option == 5:
            joinCourse()
        elif option == 6:
            markStudent()
        elif option == 7:
            f = open("students.txt", "r")
            print(f.read())
        else:
            print("Invalid option!!!")
        print("--------------------------------------------")