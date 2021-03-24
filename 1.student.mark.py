print('Welcome to Student Management simulator!')

def initStudyGroup():
    studyGroup = []

    return studyGroup

def addStudents(studyGroup):
    Student = {
        "Id": "",
        "Name": "",
        "DoB": ""
    }
    
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
    course = {
        "Id": "",
        "Name": "",
        "Mark": []
    }
    
    id = input("Id: ")
    course.update({"Id": id})
    name = input("Name: ")
    course.update({"Name": name})

    Courses.append(course)

def displayStudent(studyGroup):
    i = 0
    for i in studyGroup:
        print (studyGroup.get("Id") + " : " + studyGroup.get("Name"))

def enrollCourse(studyGroup, Courses):
    mark = {
        "Name": "",
        "Mark": 0.0
    }

    print("Which course are they enrolling for?")
    i = 0
    for i in Courses:
        print("   " + i+1 + " : " + Courses[i].get("Name") )
    
    n = input()
    while (n > Courses.len()+1):
        print("Course not found! Try another one?")
        n = input()
    
    print("Who will enroll in this course?")
    

    
    id = input()
    i = 0
    for i in studyGroup:
        if studyGroup[i]("Id") == id:
            mark.update({"Name": studyGroup[i].get("Name")})
            Courses[n-1]["Mark"].append(mark)

    print("who else will enroll in this course")
    print("0 : No one else.")
    id = input()
    while id != 0:
        i = 0
        for i in studyGroup:
            if studyGroup[i]("Id") == id:
                mark.update({"Name": studyGroup[i].get("Name")})
                Courses[n-1]["Mark"].append(mark)

    
    


studyGroup = initStudyGroup()
Courses = initCourses()

addStudents(studyGroup)
addStudents(studyGroup)
addStudents(studyGroup)

displayStudent(studyGroup)