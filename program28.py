name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

username = name[:3] + roll_no[-2:]

print("Generated username:", username)