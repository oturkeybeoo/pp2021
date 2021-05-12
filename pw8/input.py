from domain import Student, Course, Mark
import math
import zipfile
import threading

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
        writeStudent()

def addCourses():
    n = (int)(input("How many course(s) you want to add? "))
    for i in range(n):
        id = (int)(input("Course's Id? "))
        name = (str)(input("Course's name? "))
        credit = (int)(input("Course's credit? "))
        course = Course(id, name, credit)
        AllCourses.append(course)
        writeCourse()

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
        writeStudent()

def calculateGPA(student):
    ttCredits = 0
    ttMarks = 0
    for course in student.CoursesList:
        ttMarks = ttMarks + course.Mark * course.Credit
        ttCredits = ttCredits + course.Credit
    if ttCredits == 0:
        gpa = 0
    else:    
        gpa = ttMarks/ttCredits
    student.GPA = round(gpa)

def writeCourse():
    f = open("courses.txt", "a")
    for course in AllCourses:
        f.write(f"{course.getId()} {course.getName()} {course.getCredit()} \n")
    f.close()

def writeStudent():
    f = open("students.txt", "a")
    for student in AllStudents:
        f.write(f"{student.getId()} {student.getName()} {student.getDoB()} {student.getGPA()} \n")
    f.close()

def readCourse(lock):
    with lock:
        f = open("courses.txt", "r")
        for line in f.readlines():
            info = line.split()
            course = Student((int)(info[0]), info[1], info[2])
            AllCourses.append(course)
    
def readStudent(lock):
    with lock:
        f = open("students.txt", "r")
        for line in f.readlines():
            info = line.split()
            student = Student((int)(info[0]), info[1], info[2])
            student.setGPA((float)(info[3]))
            AllStudents.append(student)

def compressFile():
    with zipfile.ZipFile("students.dat", "w") as zf:
        zf.write("students.txt")
        zf.write("courses.txt")
        