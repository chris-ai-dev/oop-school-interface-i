#to use the all_students from/import
#because using runner file , use from classes. import 
from classes.student import Student
from classes.staff import Staff

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.load_all_staff()
        #to call load_all_student() use the method
        self.students = Student.load_all_students()
