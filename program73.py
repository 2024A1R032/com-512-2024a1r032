# program to input numbers in a list and find the second largest
ls = list(map(int,input().split()))
first=float("-inf")
second=float("-inf")
for i in ls:
    if i > first:
        second=first
        first=i
    elif i>second and i<first:
        second=i
print("second largest: ",second)