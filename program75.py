# input in a list and create a separate list for even and odd numbers
ls=list(map(int,input("enter numbers: ").split()))
even_lst=[]
odd_lst=[]
for x in ls:
    if x%2==0:
        even_lst.append(x)
    else:
        odd_lst.append(x)
print(odd_lst)
print(even_lst)