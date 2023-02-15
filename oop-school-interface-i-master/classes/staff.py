from .person import Person
import csv

class Staff(Person):
    def __init__(self, name, age, password, role, employee_id):
        super().__init__(name, age, password, role) 
        self.employee_id = employee_id
        

    def all_staff():
        staff_csv = []
        data = open('/Users/reapingcalamity/Desktop/TangoPlatoon/Assignments/oop-school-interface-i-master/data/staff.csv')
        reader = csv.DictReader(data)
        for row in reader:
            staff_csv.append(row)
        data.close()
        return f"{staff_csv}"