import math
import numpy

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

    def setDoB(self, dob):
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
    Credits: int
    StudentsList: []

    def __init__(self, id, name, credit):
        self.Id = id
        self.Name = name
        self.Credits = credit
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