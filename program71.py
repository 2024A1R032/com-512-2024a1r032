# program to print marks of n students in a list display highest marks,lowest marks,average marks and number of student who passed
n=int(input("enter n : "))
number_lst=list(map(int,input("enter the marks of students : ").split()))
print("Max marks: ",max(number_lst))
print("Lowest marks: ",min(number_lst))
print("Average marks: ",sum(number_lst)//len(number_lst))