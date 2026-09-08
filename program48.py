correct_pin="2850"
while True:
    pin=input("enter 4 digit pin: ")
    if len(pin)!=4:
        print("pin must be exactly 4 digits")
        continue
    if pin==correct_pin:
            print("lock opened")
            break
    else:
        print("wrong pin.try again")    
# pin=input("enter the 4- digit pin: ")
# if len(pin)==4 and pin.isdigit():
#     print("the lock is opened")
# else:
#     print("wrong pin ! enter again ")

