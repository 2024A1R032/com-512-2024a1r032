# write the python program to fill the given letter template with name and date
letter='''
dear <Name>,
you are selected!
<Date>
'''
name=input("enter name: ")
date=input("enter date: ")
letter=letter.replace("<Name>",name)
letter=letter.replace("<Date>",date)
print(letter)