# python program to store multiple student records as a list of tuples . each tuple should cotain name,rollnumber, and marks . display students who scored above 75
student_records = [
    ("Alice", 101, 82),
    ("Bob", 102, 65),
    ("Charlie", 103, 90),
    ("David", 104, 74),
    ("Eva", 105, 78)
]
print("Students who scored above 75:")
for student in student_records:
    name, roll_number, marks = student
    if marks > 75:
        print(f"Name: {name}, RollNumber: {roll_number}, Marks: {marks}")
