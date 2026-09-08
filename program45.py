name=input("enter the name: ")
branch=input("enter the branch: ")
year=input("enter the year: ")
code_name=name[:3]+"-"+branch[:3]+"-"+year[-2:]
print("*" * 30)
print("student_code: ",code_name)
print("*" * 30)