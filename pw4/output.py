import domain
from input import *

def options():
    print("""What do yo want to do?:
    1 List students.
    2 List courses.
    3 Add student to the study group.
    4 Add course to study.
    5 Add student to course.
    6 Mark student in the course.
    7 Get student GPA.
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
        else:
            print("Invalid option!!!")
        print("--------------------------------------------")