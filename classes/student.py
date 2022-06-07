from classes.person import Person
# import csv
# #import os is for fetching its contents, folder/directory
# import os

class Student(Person):
    def __init__(self, name, age, role, school_id, password):
        #using name = name allows for out of order and use
        #take them as keyword values (called kwargs
        super().__init__(name=name, age=age, role=role, password=password)
        self.school_id = school_id

    
    #create a class method load_all_students, student calls will be in charge of talking to our student database
    @classmethod
    def load_all_students(cls):
        # #store all students in a list
        # all_students = []
        # my_path = os.path.abspath(os.path.dirname(__file__))
        # file = os.path.join(my_path, "../data/students.csv")
        # with open(file, mode='r') as csvfile:
        #     dict_reader = csv.DictReader(csvfile)
        #     for row_dict in dict_reader:
        #         #create student instances - multiple 
        #         #use ** use kwargs
        #         student = Student(**row_dict)
        #         all_students.append(student)
        
        # return all_students
        #moved the above code to person, now just call the function
        return super().load_all_people("../data/students.csv")
        
    
    #to return human readable code use __str__
    def __repr__(self):
        return f"Students: {self.name}, {self.age,}, {self.role}, {self.school_id}, {self.password}"         