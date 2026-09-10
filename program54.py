#python program that asks the user to enter a username and password.the user should get only 3 attempts.
Password='abc@123'
username="john doe"
for i in range(3):
    cusername=input("enter the username: ")
    cpassword=input("enter your password: ")
    if cusername==username and cpassword==Password:
        print("login successfull")
    else:
        print("Invalid credentials.please try again")
        
