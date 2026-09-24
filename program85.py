# python program to store one student data as a tuple : name,rollno , and marks . display grade based on marks
name = input("Enter Student Name: ")
roll_no = int(input("Enter Roll Number: "))
marks = float(input("Enter Marks (out of 100): "))
student_data = (name, roll_no, marks)
score = student_data[2]  
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 50:
    grade = "E"
else:
    grade = "F (Fail)"
print(f"Name:        {student_data[0]}")
print(f"Roll Number: {student_data[1]}")
print(f"Marks:       {student_data[2]}")
print(f"Grade:       {grade}")
