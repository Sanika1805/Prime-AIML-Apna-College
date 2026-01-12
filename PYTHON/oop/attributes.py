# types
#1)nclass attributes -> belogs to class, common
#2) instance -> belongs to object, unique

class Student:
    college_name = "NBNSTIC" #class attributes
    PI = 3.14
    def __init__(self, name, cgpa):
        self.name = name #instance attibutes which are define by self
        self.cgpa = cgpa
        self.PI = 3.1

stu1 = Student("Sanika", 8.8)
print(stu1.name) #should write obj name if class name write then error occurs
print(stu1.college_name) #can call anyones name
print(stu1.PI) #if both have same name then obj parametere given higher priority
print(Student.PI) # here we get class attributes

