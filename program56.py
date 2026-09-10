# import math
# a=int(input("enter the ist number: "))
# b=int(input("enter the 2nd number: "))
# result=math.gcd(a,b)
# print("the gcd of ist and 2nd number  is :",result)


a=int(input("enter the first number: "))
b=int(input("enter the 2nd number: "))
num1,num2 =a,b
while b!=0:
    remainder=a%b 
    a=b
    b=remainder
    print(f"the GCD of {num1} and {num2} is {a}")