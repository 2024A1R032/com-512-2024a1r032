password=input("enter the password: ")
presence=password.find('@')
char=password !=password[-1]
print("length: ",len(password))
print("presence of @: ",presence)
print("check if first and last characters are different: ",char)