a=int(input("enter the 2 digit number: "))
sum=a%10
a//=10
sum+=a
print(f"sum of the digits is: {sum }")