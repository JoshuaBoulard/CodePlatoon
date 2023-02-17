from classes.school import School
from classes.person import Person
from classes.staff import Staff
from classes.student import Student

school = School('Ridgemont High') 

count = 0
while count == 0:

    mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")

    if mode == '1':
        school.list_students()
    elif mode == '2':
        student_id = input('Enter student id: ')
        student = school.find_student_by_id(student_id)
        print(str(student))
    elif mode == '5':
        count += 1
        print('Have a nice day!')   
    else:
        pass 

