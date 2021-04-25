import math
import numpy
import curses

class Student:
    Id: int
    Name: str
    DoB: str
    GPA: float
    CoursesList: []

    def __init__(self, id, name, dob):
        self.Id = id
        self.Name = name
        self.DoB = dob
        self.GPA = 0.0
        self.CoursesList = []
    
    def setId(self, id):
        self.Id = id
    
    def setName(self, name):
        self.Name = name

    def setBoB(self, dob):
        self.DoB = dob
    
    def setGPA(self, gpa):
        self.GPA = gpa
    
    def getId(self):
        return (int)(self.Id)
    
    def getName(self):
        return (str)(self.Name)

    def getDoB(self):
        return (str)(self.DoB)
    
    def getGPA(self):
        return (float)(self.GPA)

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
            GPA: {self.getGPA()}
            DoB: {self.getDoB()}
            No.Course: {len(self.CoursesList)}
         """)


    
class Course:
    Id: int
    Name: str
    Credit: int
    StudentsList: []

    def __init__(self, id, name, credit):
        self.Id = id
        self.Name = name
        self.Credit = credit
        self.StudentsList = []
    
    def setId(self, id):
        self.Id = id
    
    def setName(self, name):
        self.Name = name
    
    def setCredit(self, credit):
        self.Credit = credit
    
    def getId(self):
        return self.Id
    
    def getName(self):
        return self.Name
    
    def getCredit(self):
        return self.Credits
    
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
    Credit: int
    Mark: float

    def __init__(self, course, student, credit):
        self.Course = course
        self.Student = student
        self.Credit = credit
        self.Mark = -1.0

    def setCourse(self, course):
        self.Course = course
    
    def setStudent(self, student):
        self.Student = student

    def setCredit(self, credit):
        self.Credit = credit
    
    def setMark(self, mark):
        self.Mark = mark
    
    def getCourse(self):
        return self.Course
    
    def getStudent(self):
        return self.Student

    def getCredit(self):
        return self.Credit
    
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
        credit = (int)(input("Course's credit? "))
        course = Course(id, name, credit)
        AllCourses.append(course)

def searchId(list, id):
    for i in list:
        if i.getId() == id:
            print(i.getName())
            return i
    
def joinCourse():
    display(AllCourses)
    course  = (int)(input("Select the course Id you want student to join: "))
    foundCourse = Course(0, "Null", 0)
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
    
    mark = Mark(foundCourse, foundStudent, foundCourse.Credit)
    foundCourse.StudentsList.append(mark)
    foundStudent.CoursesList.append(mark)

def round(mark):
    return (math.floor(10 * mark))/10

def markStudent():
    display(AllCourses)
    course = (int)(input("Which course do you want to give marks? "))
    foundCourse = Course(0, "Null", 0)
    foundCourse = searchId(AllCourses, course)
    while not foundCourse:
        course = (int)(input("Course not found! Try again? "))
        foundCourse = searchId(AllCourses, course)
    
    for student in foundCourse.StudentsList:
        print(f"Student: {student.Student}")
        mark = (float)(input("Input mark for this student: "))
        student.Mark = round(mark)

def calculateGPA(student):
    ttCredis = 0
    ttMarks = 0
    for course in student.CoursesList:
        ttMarks = ttMarks + course.Mark * course.Credit
        ttCredis = ttCredis + course.Credit
    if ttCredis == 0:
        gpa = 0
    else:    
        gpa = ttMarks/ttCredis
    student.GPA = round(gpa)

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

StudentMarkManagement()

# def main(stdscr):

# curses.wrapper(main)