#python program to input two lists and create a third list containing common elements
ls=list(map(int,input("enter numbers: ").split()))
ls_1=list(map(int,input("enter numbers: ").split()))
lst=[]
for x in ls:
    if x in ls_1:
        lst.append(x)
print(lst)