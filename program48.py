pin=input("enter the pin: ")
if len(pin)==4 and pin.isdigit():
    print("the lock is opened")
else:
    print("wrong pin ! enter again ")