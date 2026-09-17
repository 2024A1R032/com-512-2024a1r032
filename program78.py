# write a python program to count how many times a particular element appears in a list
ls=list(map(int,input("enter numbers: ").split()))
freq={}
for i in ls:
    freq[i]=freq.get(i,0)+1
print(freq)