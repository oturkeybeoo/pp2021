class Student:
    Id: int
    Name: str
    DoB: str
    CoursesList: []

    def __init__(self, id, name, dob):
        self.Id = id
        self.Name = name
        self.DoB = dob
        self.CoursesList = []
    
    def setId(self, id):
        self.Id = id
    
    def setName(self, name):
        self.Name = name

    def setBoB(self, dob):
        self.DoB = dob
    
    def getId(self):
        return (int)(self.Id)
    
    def getName(self):
        return (str)(self.Name)

    def getDoB(self):
        return (str)(self.DoB)

    def getMark(self):
        for mark in self.CoursesList:
            print(f"""
                Course: {mark.Course}
                Mark: {mark.Mark}
            """)
    
    """def getResult(self):
        mark: {
            "Course": "",
            "Mark": -1.0
        }
        result: []

        for crs in self.CoursesList:
            mark.update({"Course": crs.Course})
            mark.update({"Mark": crs.Mark})
            result.append(mark)

        return result"""
    
    def toString(self):
        print(f"""
            Id: {self.getId()}
            Name: {self.getName()}
            DoB: {self.getDoB()}
            No.Course: {len(self.CoursesList)}
         """)


    
class Course:
    Id: int
    Name: str
    StudentsList: []

    def __init__(self, id, name):
        self.Id = id
        self.Name = name
        self.StudentsList = []
    
    def setId(self, id):
        self.Id = id
    
    def setName(self, name):
        self.Name = name
    
    def getId(self):
        return self.Id
    
    def getName(self):
        return self.Name
    
    def getMark(self):
        for mark in self.StudentsList:
            print(f"""
                Student: {mark.Student}
                Mark: {mark.Mark}
            """)

    """def getMark(self):
        mark: {
            "Student": "",
            "Mark": -1.0
        }
        result: []

        for std in self.StudentsList:
            mark.update({"Student": std.Student})
            mark.update({"Mark": std.Mark})
            result.append(mark)
        
        return result"""
    
    def toString(self):
        print(f"""
            Id: {self.getId()}
            Name: {self.getName()}
            No.Students: {len(self.StudentsList)}
        """)

class Mark:
    Course: str
    Student: str
    Mark: float

    def __init__(self, Course, Student):
        self.Course = Course
        self.Student = Student
        self.Mark = -1.0

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

    def display4Course(self):
        print(f"""
            Student: {self.Student}
            Mark: {self.Mark}
        """)

    

AllStudents = []
AllCourses = []

def display(list):
    for i in list:
        i.toString()

"""def displayCourses(AllCourses):
    for course in AllCourses:
        course.toString()"""

def addStudents():
    n = (int)(input("How many student(s) you want to add? "))
    for i in range(n):
        id = (int)(input("Student's Id? "))
        name = (str)(input("Student's name? "))
        dob = (str)(input("Student's Date of Birth? "))
        student = Student(id, name, dob)
        AllStudents.append(student)

def addCourses():
    n = (int)(input("How many course(s) you want to add? "))
    for i in range(n):
        id = (int)(input("Course's Id? "))
        name = (str)(input("Course's name? "))
        course = Course(id, name)
        AllCourses.append(course)

def searchId(list, id):
    for i in list:
        if i.getId() == id:
            print(i.getName())
            return i
    
def joinCourse():
    display(AllCourses)
    course  = (int)(input("Select the course Id you want student to join: "))
    foundCourse = Course(0, "Null")
    foundCourse = searchId(AllCourses, course)        
    while not foundCourse:
        course = (int)(input("Course not found! Try again? "))
        foundCourse = searchId(AllCourses, course) 

    display(AllStudents)
    student = (int)(input("Select the Id of the student will join this course: "))
    foundStudent = Student(0, "Null", "Null")
    foundStudent = searchId(AllStudents, student)
    while not foundStudent:
        student = (int)(input("Student not found? Try again? "))
        foundStudent = searchId(AllStudents, student)
    
    mark = Mark(foundCourse, foundStudent)
    foundCourse.StudentsList.append(mark)
    foundStudent.CoursesList.append(mark)
        
def markStudent():
    display(AllCourses)
    course = (int)(input("Which course do you want to give marks? "))
    foundCourse = Course(0, "Null")
    foundCourse = searchId(AllCourses, course)
    while not foundCourse:
        course = (int)(input("Course not found! Try again? "))
        foundCourse = searchId(AllCourses, course)
    
    for student in foundCourse.StudentsList:
        print(f"Student: {student.Student}")
        mark = (float)(input("Input mark for this student: "))
        student.Mark = mark
        
def options():
    print("""What do yo want to do?:
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

StudentMarkManagement()


"""stA = Student(1, "A", "Jan")
stB = Student(2, "B", "Feb")
crs1 = Course(101, "Math")
crs2 = Course(102, "Chem")
AllStudents.append(stA)
AllStudents.append(stB)
AllCourses.append(crs1)
AllCourses.append(crs2)
joinCourse()"""