#program name: Assignment2.py
#Course: IT3883/Section W01
#Juan Martinez
#Assignment #2
#Due Date: 10/02/2026
#Purpose: To take the grades of the students average them out and sort them
# out from highest to lowest. 
#Specific resources: lessons and online examples.

file = open("Assignment2input.txt", "r")

students = []

for a in file:
    info = a.split()

    names = info[0]
    grades = list(map(int, info[1:]))

    avg = sum(grades) / len(grades)

    students.append([names, avg])

file.close()

for b in range(len(students)):
    greatest = b

    for c in range(b + 1, len(students)):
        if students[c][1] > students[greatest][1]:
            greatest = c

    students[b], students[greatest] = students[greatest], students[b]

for student in students:
    print(student[0], round(student[1], 2))