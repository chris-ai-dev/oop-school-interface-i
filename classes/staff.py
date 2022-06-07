from classes.person import Person
# import csv
# import os

class Staff(Person):
    def __init__(self, name, age, role, employee_id, password):
        #using name = name allows for out of order and use
        #take them as keyword values (called kwargs
        super().__init__(name=name, age=age, role=role, password=password)
        self.employee_id = employee_id
        
    #create a class method load_all_students, student calls will be in charge of talking to our student database
    @classmethod
    def load_all_staff(cls):
        # #store all students in a list
        # all_staff = []
        # my_path = os.path.abspath(os.path.dirname(__file__))
        # file = os.path.join(my_path, "../data/staff.csv")
        # with open(file, mode='r') as csvfile:
        #     dict_reader = csv.DictReader(csvfile)
        #     for row_dict in dict_reader:
        #         #create student instances - multiple 
        #         #use ** use kwargs
        #         staff = Staff(**row_dict)
        #         all_staff.append(staff)
        
        # return all_staff
         #moved the above code to person, now just call the function
        return super().load_all_people("../data/staff.csv")
       
    #to return human readable code use __str__ or use __repr__
    def __repr__(self):
        return f"Staff: {self.name}, {self.age,}, {self.role}, {self.employee_id}, {self.password}"   