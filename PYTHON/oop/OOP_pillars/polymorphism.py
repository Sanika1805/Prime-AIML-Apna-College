#many form
#multiple fnx but with same name
#eg -> operator overloading
#types -> function overriding & duck typing

# #Fnx overriding -> have parent & child class and redefining parent class's fnx in child class
# class Employee:
#     def get_designation(self):
#         print("designation = Employee")

# class Teacher(Employee):
#     def get_designation(self):
#         print("designation = Teacher")

# t1 = Teacher()
# t1.get_designation()


#Duck typing
class Teacher(Employee):
    def get_designation(self):
        print("designation = Teacher")

class Accountant():
    def get_designation(self):
        print("designation = Accountant")

t1 = Teacher()
t1.get_designation()

acc1 = Accountant()
acc1.get_designation()
