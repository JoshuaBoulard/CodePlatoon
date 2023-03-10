from .person import Person
import csv

class Student(Person):
    def __init__(self, name, age, password, role, school_id):
        super().__init__(name, age, password, role) 
        self.school_id = school_id
    
    def __str__(self):
        return f'\n{self.name.upper()}\n----------\nage: {self.age}\npassword: {self.password}\nrole: {self.role}\nschool id: {self.school_id}'

    def all_students():
        students_csv = []
        data = open('/Users/reapingcalamity/Desktop/TangoPlatoon/Assignments/oop-school-interface-i-master/data/students.csv')
        reader = csv.DictReader(data)
        for row in reader:
            students_csv.append(Student(**row))
        data.close()
        return students_csv