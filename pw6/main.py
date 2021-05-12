from output import StudentMarkManagement
from input import readCourse, readCourse
import zipfile
import os

if os.path.isfile("students.dat"):
    with zipfile.ZipFile("students.dat", "r") as zf:
        zf.extractall()


StudentMarkManagement()