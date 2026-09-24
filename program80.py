#write a python program to store two points as tuples and calculate the distance between them

import math
x1=int(input("enter x1: "))
x2=int(input("enter x2: "))
x3=int(input("enter x3: "))
x4=int(input("enter x4: "))
point1=(x1,x2)
point2=(x3,x4)
distance=math.dist(point1,point2)
print(distance)