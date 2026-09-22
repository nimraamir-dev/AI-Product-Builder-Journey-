students = [
    {"name": "Ali", "marks": 5000},
    {"name" : "Ahmad", "marks": 1000},
    {"name": "Bilal", "marks": 3000}
]
def sort_by_marks(data):
    return sorted(data, key=lambda x:x["marks"])
sorted_students = sort_by_marks(students)
print(sorted_students)