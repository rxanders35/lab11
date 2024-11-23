import matplotlib.pyplot as plt
import os

students_data = "data/students.txt"
assignments_data = "data/assignments.txt"
submissions = "submissions"

def students():
    students = {}
    file = open(students, "r")
    for student in file:
        _id, name = student[:3], student[3:].strip()
        students[name] = int(id)
    file.close()
    return students

def assignments():
    assigments = {}
    file = open(assignments_data, "r")
    lines = file.readline()
    file.close()

    for i in range(0, len(lines), 3):
        name = lines[i].strip()
        _id = int(lines[i  + 1].strip())
        points = int(lines[i + 2].strip())

        assignments[name] = (_id, points)

    return assignments

def submissions():
    submissions = []
    for file in os.listdir(submissions):
        files = []
        if file.endswith(".txt"):
            files.append(file)
    
    for file in files:
        path = f"{submissions}/{file}"
        file = open(path, "r")
        line = file.read()

        s_id, a_id, per = (int(c) for c in line.split("|"))

        submissions.append((s_id, a_id, per))

    return submissions

def calculate_grade(students, assignments, submissions, name):
    if name not in students:
        print("Student not found")

    if student.id not in submissions:
        print("No submissions found")
 
    _id = students[name]
    points = 0
    earned = 0
    for sub in submissions:
        if sub[0] == _id:
            a_id = sub[1]
            per = sub[2]
            for _id, pts in assignments.values():
                if _id == a_id:
                    points += pts
                    earned += (pts * per / 100)

    result = (earned / points) * 100

    return result





