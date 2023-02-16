from .student import Student
from .staff import Staff

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()

    def list_students(self):
        for student in range(len(self.students)):
            print(f'{student + 1}. {self.students[student].name} {self.students[student].school_id}')

    def find_student_by_id(self, x):
        for student in range(len(self.students)):
            if self.students[student].school_id == x:
                return self.students[student]
