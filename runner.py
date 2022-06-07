from classes.school import School 
from classes.student import Student
from classes.staff import Staff

school = School('Ridgemont High') 

# print(school.name)

# student_info = {
#     'name': 'Screech',
#     'school_id': '4680',
#     'age': '17',
#     'role': 'student',
#     'password':'robots!',
#     'gpa': '3.9'
# }

# student = Student(**student_info)
# print(student.name)

# Student.load_all_students()

# for student_info in school.students:
#     print(student_info)
#     if student_info.name == 'Jessie':
#         print(student_info.age)

# Staff.load_all_staff()

# for staff_info in school.staff:
#     print(staff_info)
#     # if staff_info.name == 'Mertz':
#     #     print(staff_info.role)

print(school.staff)
print(school.students)