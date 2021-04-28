from output import *
from input import *
import zipfile
import os

if os.path.isfile("students.dat"):
    with zipfile.ZipFile("students.dat", "r") as zf:
        zf.extractall()

readStudent()
readCourse()

StudentMarkManagement()