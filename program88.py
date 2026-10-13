"""
create a class and object : student details
problem: create a student class to store a students name and roll number 
create an object and display the details using an instance method
"""
class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
student_a=Student("Abhimanyu","32")
print("student details: ",student_a.name)
print("student details: ",student_a.roll)
