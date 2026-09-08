student = input("enter the student name: ")
attendance = int(input("enter attendance: "))
cgpa = float(input("enter the cgpa: "))
hackathon_input = input("enter the hackathon (true/false): ").strip().lower()
hackathon = hackathon_input in ["true", "yes"]
if cgpa >= 8.5 and hackathon and attendance >= 85:
    print("student is eligible")
else:
    print("student is not eligible")
