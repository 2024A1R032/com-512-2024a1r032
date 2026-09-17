# program to input marks of 10 students .store only valid marks between 0 and 100 in a list .skip invalid marks
valid_marks = []
for i in range(10):
    marks=int(input("enter marks: "))
    if marks<0 and marks>100:
        continue
    valid_marks.append(marks)
    print("Valid marks list: ",valid_marks)

