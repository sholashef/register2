students_name = [] # Initialize an empty School Register
while True:
    name =input("Enter new student name")
    # Check if the user wants to stop
    if name.lower() == "":
        break
    students_name.append(name)#Add the entered value to the list
    print(students_name)# Print the updated list
