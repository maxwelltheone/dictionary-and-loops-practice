# Alright, let's simplify and rephrase the problem set to avoid using functions:
import student_data

# print(student_data.students)
students = student_data.students
# print(len(students))
# print(students[0]['Combo,Name'])
# print(students[0]['Email'][0])
# print(students[0]['Email'][1])
# print(students[0]['HR'])
# print(students[0]['GL'])
# print(students[0]['CPSID'])

# for loops allow us to
#iterate through the data
#and perform some function

#we are iterating through the data
#and printing the name and email of the students
#we are also printing a line of underscores to separate the students
#we are also printing a line of underscores to separate the students
# for student in students:
#     print(student['Combo,Name'])
#     print(student['Email'][0])
#     print(student['Email'][1])
#     print("_"*25)


# we are asking the user to input their name
# then we are checking if the name is in the data
# if the name is in the data we are printing the name and "this works"
# name = input("what is your name?") 
# id = int(input("What is your ID?"))
# for student in students:
#     if id == student['CPSID']:
#         print(student['Combo,Name'])
#         print("this works")

# # Let's try to print out the emails of the students:    

# for student in students:
#     print(student['Combo,Name'])
#     print(student['Email'][0])
#     print(student['Email'][1])
#     print("_"*25)

# Update the dataset in memory (e.g., modify student details)
for student in students:
    if student['CPSID'] == 10000011:  # Example CPSID to update
        student['FName'] = 'Mason'
        student['LName'] = 'Paulo'\



for student in students:
    if student['CPSID'] == 1000036:  # Replace with the condition to find the specific student
        del student['MName']  # Deletes the 'MName' key-value pair
        print(f"Updated student: {student}")

# Update a specific entry by index
students[2]['FName'] = 'Niloticus'  # Updates the first student's first name
students[2]['LName'] = 'Shangnin'
print(students[3])


#Adding 'contactNumber' field to each student
for student in students:
    if student['CPSID'] == 1000015:
        student['contactNumber'] = '773-864-4437'


# Example: Update multiple fields for students in a specific homeroom
for student in students:
    if student['HR'] == 'B211':  # Condition to find specific students
        student.update({
            'FName': 'UpdatedFirstName',
            'LName': 'UpdatedLastName',
            'Email': ['new.email@example.com', 'secondary.email@example.com']
        })
        print(f"Updated student: {student}")




# Overwrite the `student_data.py` file with the updated data
# Overwrite the student_data.py file with formatted data
with open('student_data.py', 'w') as f:
    f.write("students = [\n")
    for student in students:
        formatted_student = "    {\n"
        for key, value in student.items():
            formatted_student += f"        '{key}': {repr(value)},\n"
        formatted_student = formatted_student.rstrip(",\n") + "\n    },\n"  # Clean trailing commas and newline
        f.write(formatted_student)
    f.write("]\n")

print("student_data.py has been updated with the original formatting.")


