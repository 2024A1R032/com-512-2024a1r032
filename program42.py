firstname=input("enter the first name: ")
lastname=input("enter the last name: ")
rollno=input("enter the rollno: ")
email=firstname[0:3]+lastname[0:3]+rollno[-3:]
print("generated username: ",email)