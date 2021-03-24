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
        "Mark": 0.0
    }

print('Welcome to Student Management simulator!')

def initStudyGroup():
    studyGroup = []

    return studyGroup

def addStudents(studyGroup):    
    id = input("Id: ")
    Student.update({"Id": id})
    name = input("Name: ")
    Student.update({"Name": name})
    dob = input("DoB: ")
    Student.update({"DoB": dob})

    studyGroup.append(Student)
    

def initCourses():
    Courses = []

    return Courses

def addCourse(Courses):    
    id = input("Id: ")
    course.update({"Id": id})
    name = input("Name: ")
    course.update({"Name": name})

    Courses.append(course)

def displayStudent(studyGroup):
    for s in studyGroup:
        print(s.get("Id") + " : " + s.get("Name"))

def displayCourses(Courses):
    for c in Courses:
        print(c.get("Id") + " : " + c.get("Name"))

def enrollCourse(studyGroup, Courses):
    print("Which course are they enrolling for?")
    displayCourses(Courses)
    
    not_found_course = True
    n = (str)(input())
    while not_found_course:
        for c in Courses:
            if n == c.get("Id"):
                not_found_course = False
                break
        if(not_found_course):
            print("Course not found! Try another one?")
            n = input()
    
    print("Who will enroll in this course?")
    displayStudent(studyGroup)

    id = (str)(input())
    for s in studyGroup:
        if s.get("Id") == id:
            mark.update({"Name": s.get("Name")})
            c["Mark"].append(mark)

    print("Who else will enroll in this course")
    print("0 : No one else.")
    displayStudent(studyGroup)

    id = (str)(input())
    while id != 0:
        for s in studyGroup:
            if s.get("Id") == id:
                mark.update({"Name": s.get("Name")})
                c["Mark"].append(mark)
        print("Who else will enroll in this course")
        print("0 : No one else.")
        displayStudent(studyGroup)
        id = (str)(input())
        if id == 0:
            break
    

    

    
    


studyGroup = initStudyGroup()
addStudents(studyGroup)
displayStudent(studyGroup)

Courses = initCourses()
addCourse(Courses)
displayCourses(Courses)

enrollCourse(studyGroup, Courses)