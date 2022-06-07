import csv
import os

class Person:
    def __init__(self, name, age, role, password):
        self.name = name 
        self.age = age
        self.role = role         
        self.password = password
        
    #use class method for loading data
    @classmethod
    def load_all_people(cls, file_name):
        #store all students in a list
        all_people = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        file = os.path.join(my_path, file_name)
        with open(file, mode='r') as csvfile:
            dict_reader = csv.DictReader(csvfile)
            for row_dict in dict_reader:
                #create student instances - multiple 
                #use ** use kwargs
                #use cls to refereto diff class so both staff and student class can call it
                person = cls(**row_dict)
                all_people.append(person)
        
        return all_people