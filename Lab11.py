import matplotlib
# I am doing this because I am using Windows Subsystem for Linux
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

students_data = "data/students.txt"
assignments_data = "data/assignments.txt"
submissions_dir = "data/submissions"

class Assignment:
    def __init__(self, name, _id, points):
        self.name = name
        self._id = _id
        self.points = points

class Student:
    def __init__(self, _id, name):
        self._id = _id
        self.name = name

def load_students():
    students = {}
    file = open(students_data, "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        _id = line[:3]
        name = line[3:].strip()
        students[_id] = Student(_id, name) 
        students[name] = students[_id]
    return students

def load_assignments():
    assignments = {}
    file = open(assignments_data, "r")
    lines = file.readlines()
    file.close()

    for i in range(0, len(lines), 3):
        name = lines[i].strip()
        _id = lines[i  + 1].strip()
        points = int(lines[i + 2].strip())
        assignment= Assignment(name, _id, points)
        assignments[_id] = assignment
        assignments[name] = assignment

    return assignments

def load_submissions():
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
    if name not in students:
        return "Student not found" 

    student = students[name]
    if student._id not in submissions:
        return "Submission not found"

    total = 0
    earned = 0

    for a_id, per in submissions[student._id].items():
        assignment = next((a for a in assignments.values() if isinstance(a, Assignment) and a._id == a_id), None)
        if assignment:
            total += assignment.points
            earned += (per / 100) * assignment.points

    if total == 0:
        return "0%"

    result = round((earned / total)* 100)
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
    a = sum(scores) / len(scores)
    ma = max(scores)

    return f"Min: {int(mi)}%\nAvg: {int(a)}%\nMax: {int(ma)}%"

def display_graph(assignments, submissions, assignment_name):
    if assignment_name not in assignments:
        return "Assignment not found"

    assignment = assignments[assignment_name]
    scores = []
    for subs in submissions.values():
        if assignment._id in subs:
            scores.append(subs[assignment._id])
    if not scores:
        return "Submissions not found"

    plt.figure() 
    plt.hist(scores, bins=[
                    50, 55, 60, 65, 
                    70, 75, 80, 85, 
                    90, 95, 100
                        ])
    plt.savefig('plot.png')
    '''
    The plt will get saved to the project directory
    instead of opened in a window due to the fact that I
    am using WSL2

    I personally DONT feel like copying the code over to
    a Windows directory and re-cloning the repo
    '''
    plt.close()
    return None

def main():

    students = load_students()
    assignments = load_assignments()
    submissions = load_submissions()
    print('''
1. Student grade
2. Assignment statistics
3. Assignment graph''')
    selection = input("\nEnter your selection: ")

    if selection == "1":
        student_name = input("What is the student's name: ")
        grade = calculate_grade(students, assignments, submissions, student_name)
        print(grade)
    elif selection == "2":
        assignment_name = input("What is the assignment name: ")
        stats = assignment_statistics(assignments, submissions, assignment_name) 
        print(stats) 
    elif selection == "3":
        assignment_name = input("What is the assignment name: ")
        result = display_graph(assignments, submissions, assignment_name)
        if result:
            print(result)

if __name__ == "__main__":
    main()





