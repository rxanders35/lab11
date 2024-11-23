import matplotlib.pyplot as plt
import os

students_data = "data/students.txt"
assignments_data = "data/assignments.txt"
submissions_dir = "submissions"

class Assignment:
    def __init__(self, name, _id, points):
        self.name = name
        self._id = _id
        self.points = points

class Student:
    def __init__(self, _id, name):
        self._id = _id
        self.name = name

def students():
    students = {}
    file = open(students_data, "r")
    lines = file.readlines()
    file.close()
    for student in file:
        _id = student[:3]
        name = student[3:].strip()
        students[_id] = Student(_id, name) 
        students[name] = students[_id]
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
        assignments[name] = Assignment(name, _id, points)
        assignments[name] = assignments[_id]

    return assignments

def submissions():
    submissions = {}
    for file in os.listdir(submissions_dir):
        f = open(os.path.join(submissions_dir, file), "r")
        line = f.readline().strip()
        f.close()

        s_id, a_id, score = line.split("|")
        if s_id not in submissions:
            submissions[s_id] = {}
        submissions[s_id][a_id] = float(score)

    return submissions

def calculate_grade(students, assignments, submissions, name):
    if student_name not in students:
        return "Student not found" 

    student = students[name]
    if student._id not in submissions:
        return "Submission not found"

    total = 0
    earned = 0

    for a_id, per in submissions[student._id].items():
        assignment = next((a for a in assignments.values() if isinstance(a, Assignment) and a._id == a_id), None)
        if assignment:
            points += assignment.points
            earned += (per / 100) * assignment.points

    result = (earned / total)* 100
    return f"{result}%"

def assignment_statistics(assignments, submissions, assignment_name):
    if assignment_name not in assignments:
        return "Assignment not found" 
    
    assignment = assignments[assignment_name]
    scores =[]
    for submission in submissions.values():
        if assignment._id in submission:
            scores.append(submission[assignment._id]) 
    if not scores:
        return "Submissions not found"
    
    mi = min(scores)
    a = round(sum(scores) / len(scores))
    ma = max(scores)

    return f"Min: {mi}%\nAvg: {a}%\nMax: {ma}%"


    

def graph(assigments, submissions, assignment_name):
    if assignment_name not in assignments:
        return "Assignment not found"

    assignment = assigments[assignment_name]
    scores = []
    for subs in submissions.values():
        if assignment._id in subs:
            scores.append(subs[assignment._id])
    if not scores:
        return "Submissions not found"
    
    plt.hist(scores, bins=[0, 25, 50, 75, 100])
    plt.show()

def main():

    students = students()
    assignments = assignments()
    submissions = submissions()
    print('''
1. Student grade
2. Assignment statistics
3. Assignment graph 
    ''')
    selection = input("\nEnter your selection: ")

    if selection == "1":
        student_name = input("What is the student's name: ")
        grade = calculate_grade(students, assignments, submissions, student_name)
        if grade is None:
            print("Student not found")
        else:
            print(f"{grade}%")
    elif selection == "2":
        assigment_name = input("What is the assignment name: ")
        









