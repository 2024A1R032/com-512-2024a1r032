password=input("enter the password: ")
while len(password)<8 or '@' not in password:
    print("weak password.try again")
    password=input("enter the password: ")
print("correct password !")
