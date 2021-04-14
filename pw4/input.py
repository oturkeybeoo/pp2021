import pw4.domain as domain

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
        for student in domain.AllStudents:
            domain.calculateGPA(student)
        option = options()
        if option == 1:
            domain.display(domain.AllStudents)
        elif option == 2:
            domain.display(domain.AllCourses)
        elif option == 3:
            domain.addStudents()
        elif option == 4:
            domain.addCourses()
        elif option == 5:
            domain.joinCourse()
        elif option == 6:
            domain.markStudent()
        else:
            print("Invalid option!!!")
        print("--------------------------------------------")