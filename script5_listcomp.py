students = [
    {"name": "Ali", "marks": 5000},
    {"name" : "Ahmad", "marks": 1000},
    {"name": "Bilal", "marks": 3000}
]
top_students = []
for student in students:
    if student["marks"] >= 2000:
        top_students.append(student["name"])

print(top_students)

students = [
    {"name": "Ali", "marks": 5000},
    {"name" : "Ahmad", "marks": 1000},
    {"name": "Bilal", "marks": 3000}
]
top_students2 = [student["name"] for student in students if student["marks"] >= 2000]
print(top_students2)