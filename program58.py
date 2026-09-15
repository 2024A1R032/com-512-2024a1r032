num=int(input("enter the number: "))
org_num=num
revnum=0
while num>0:
    revnum=revnum*10+num%10
    num=num//10
    print("the reverse is : ",revnum)