from output import *
from input import *
import zipfile
import os
import threading

if os.path.isfile("students.dat"):
    with zipfile.ZipFile("students.dat", "r") as zf:
        zf.extractall()

    lock = threading.Lock()
    thread1 = threading.Thread(target=readCourse(lock))
    thread2 = threading.Thread(target=readStudent(lock))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

StudentMarkManagement()