import matplotlib.pyplot as plt

student_data = "data/students.txt"
assignments_data = "data/assignments.txt"
submissions = "submissions"

def students():
    students = {}
    file = open(student_data, "r")
    for i in file:
        student_name = line[3:]