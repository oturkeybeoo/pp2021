Student = {
        "Id": "",
        "Name": "",
        "DoB": ""
    }

course = {
        "Id": "",
        "Name": "",
        "Mark": []
    }

mark = {
        "Name": "",
        "Mark": -1.0
    }

studyGroup = []

Courses = []

def addStudents(studyGroup):    
    id = input("Id: ")
    Student.update({"Id": id})
    name = input("Name: ")
    Student.update({"Name": name})
    dob = input("DoB: ")
    Student.update({"DoB": dob})

    studyGroup.append(Student)
    print(f"{name} added to the study group.")

def addCourse(Courses):    
    id = input("Id: ")
    course.update({"Id": id})
    name = input("Name: ")
    course.update({"Name": name})

    Courses.append(course)

def displayStudent(studyGroup):
    print(f"There are {len(studyGroup)} student in the study group!")
    for s in studyGroup:
        print(s.get("Id") + " : " + s.get("Name"))

def displayCourses(Courses):
    print(f"There are {len(Courses)} courses to study!")
    for c in Courses:
        print(c.get("Id") + " : " + c.get("Name"))

def enrollCourse(studyGroup, Courses):
    print("Which course are they enrolling for?")
    displayCourses(Courses)
    
    not_found_course = True
    courseId = (str)(input())
    while not_found_course:
        for c in Courses:
            if c.get("Id") == courseId:
                not_found_course = False
                break
        if(not_found_course):
            print("Course not found! Try another one?")
            n = input()

    print("Who will enroll in this course")
    print("0 : No one.")
    displayStudent(studyGroup)

    studentId = (str)(input())
    while studentId != 0:
        for s in studyGroup:
            if s.get("Id") == studentId:
                mark.update({"Name": s.get("Name")})
                c["Mark"].append(mark)
        print("Who else will enroll in this course")
        print("0 : No one else.")
        displayStudent(studyGroup)
        studentId = (str)(input())
        
    

    
def options():
    print("""What do yo want to do?:
    1 List students.
    2 List courses.
    3 Add student to the study group.
    4 Add course to study. 
    5 Mark student in the course.
--------------------------------------------
    """)
    option = int(input())
    return option

def StudentMarkManagement():
    print("Welcome to Student Management Program!")
    while True:
        print("--------------------------------------------")
        option = options()
        if option == 1:
            displayStudent(studyGroup)
        elif option == 2:
            displayCourses(Courses)
        elif option == 3:
            addStudents(studyGroup)
        elif option == 4:
            addCourse(Courses)
        else:
            print("Invalid option!!!")
        print("--------------------------------------------")

StudentMarkManagement()