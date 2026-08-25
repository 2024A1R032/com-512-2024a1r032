# calculate the simple interest and print it
p=int(input("enter the principal: "))
r=int(input("enter the rate: "))
t=int(input("enter the time: "))
si=(p*r*t)/100
amt=p+si
print("simple_interest: ",si)
print("amount is: ",amt)
