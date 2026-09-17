#unique in list
lss=[]
ls=list(map(int,input("enter numbers: ").split()))
for i in ls:
    if i in lss:
        continue
    else:
        lss.append(i)
print(lss)
