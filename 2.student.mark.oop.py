AllStudents = []
AllCourses = []


class Student:
    Id: int
    Name: str
    DoB: str
    CoursesList: []

    def __init__(self, id, name, dob):
        self.Id = id
        self.Name = name
        self.BoB = dob
    
    def setId(self, id):
        self.Id = id
    
    def setName(self, name):
        self.Name = name

    def setBoB(self, dob):
        self.DoB = dob
    
    def getId(self):
        return self.Id
    
    def getName(self):
        return self.Name

    def getDoB(self):
        return self.DoB
    
    def getResult(self):
        mark: {
            "Course": "",
            "Mark": -1.0
        }
        result: []

        for crs in self.CoursesList:
            mark.update({"Course": crs.Course})
            mark.update({"Mark": crs.Mark})
            result.append(mark)

        return result
    
    def toString(self):
        print(f"""
            Id: {self.getId}
            Name: {self.getName}
            DoB: {self.getDoB}
            No.Course: {len(self.CoursesList)}
            \n
         """)


    
class Course:
    Id: int
    Name: str
    StudentsList: []

    def __init__(self, id, name):
        self.Id = id
        self.Name = name
    
    def setId(self, id):
        self.Id = id
    
    def setName(self, name):
        self.Name = name
    
    def getId(self):
        return self.Id
    
    def getName(self):
        return self.Name
    
    def getMark(self):
        mark: {
            "Student": "",
            "Mark": -1.0
        }
        result: []

        for std in self.StudentsList:
            mark.update({"Student": std.Student})
            mark.update({"Mark": std.Mark})
            result.append(mark)
        
        return result
    
    def toString(self):
        print(f"""
            Id: {self.getId}
            Name: {self.getName}
            No.Students: {len(self.StudentsList)}
            \n
        """)

class Mark:
    Course: str
    Student: str
    Mark: float

    def __init__(self, Course, Student, Mark):
        self.Course = Course
        self.Student = Student
        self.Mark = Mark

    def setCourse(self, course):
        self.Course = course
    
    def setStudent(self, student):
        self.Student = student
    
    def setMark(self, mark):
        self.Mark = mark
    
    def getCourse(self):
        return self.Course
    
    def getStudent(self):
        return self.Student
    
    def getMark(self):
        return self.Mark

def displayStudent(AllStudents):
    for student in AllStudents:
        student.toString()

def displayCourses(AllCourses):
    for course in AllCourses:
        course.toString()

def addStudents():
    n = (int)(input("How many student(s) you want to add? "))
    for i in n:
        id = (int)(input("Student's Id? "))
        name = (str)(input("Student's name? "))
        dob = (str)(input("Student's Date of Birth? "))
        student = Student(id, name, dob)
        AllStudents.append(student)

def addCourses():
    n = (int)(input("How many course(s) you want to add? "))
    for i in n:
        id = (int)(input("Course's Id? "))
        name = (str)(input("Course's name? "))
        course = Course(id, name)
        AllCourses.append(course)



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
            displayStudent(AllStudents)
        elif option == 2:
            displayCourses(AllCourses)
        elif option == 3:
            addStudents()
        elif option == 4:
            addCourses()
        else:
            print("Invalid option!!!")
        print("--------------------------------------------")

StudentMarkManagement()