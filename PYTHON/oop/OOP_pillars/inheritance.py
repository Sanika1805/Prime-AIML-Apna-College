# #Reusing attr & from a paret (Base) class
# class Employee:
#     start_time = "10am"
#     end_time = "6pm"

#     def change_times(self, new_end_time):
#         self.end_time = new_end_time

# class Teacher(Employee):
#     def __init__(self, subject):
#         self.subject = subject

# class Adminstaff(Employee):
#     def __init__(self, role):
#         self.role = role

# t1 = Teacher("Maths")
# t1.change_times("5pm")
# adm1 = Adminstaff("maneger")
# print(t1.subject, t1.start_time, t1.end_time)
# print(adm1.role, adm1.start_time, adm1.end_time)


# ## Types of inheritance

# #1) single level inheritance
# #2) multi level inheritance
# class Employee:
#     start_time = "10am"
#     end_time = "6pm"

# class Adminstaff(Employee):
#     def __init__(self, role):
#         self.role = role

# class Accountant(Adminstaff):
#       def __init__(self, salary, role):
#         super().__init__(role) #super keyword to pass value of role from parent class
#         self.salary = salary

# acc1 = Accountant(25_000, "CA")

# print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)


#3) multiple inheritance
class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher, Student):
    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name

ta1 = TA(25_000, 8.8, "sanika")
print(ta1.name, ta1.gpa, ta1.salary)