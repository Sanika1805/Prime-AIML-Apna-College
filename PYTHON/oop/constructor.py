#_init_Mrthode  means constuctor of the class
# use to initialize the object
# it is a special methode which is called every time when object is created
# if does not write _init_methode then python automatically write it 
#eg:  
# class Student:
#       subject = "Python"
#stu1 = Student() #() shows that _init_methode is called
#print(stu1.subject)

#synthax
#def _init_(self)  //self is a parameter means it is storing the current instance of the class or storing referance to the current object 
#we can also write _init_(abc)
# (self) is a compulsory parameteter which write in all instance methods
# self authomatically pass into methos
# #eg:
# class Student:
#     def __init__(self):
#         print("constructor was called..") #this line will print for each obj
# stu1 = Student()
# stu2 = Student()


#if want to pass individual parameter to each obj the define it while inti constructor also with self as self is default one
#eg :
# class Student:
#     def __init__(self, name, cgpa):
#         self.name = name #self.name is memory value which we are store and name is which we passing to the constructor
#         self.cgpa = cgpa
#         print("constructor was called..")

# stu1 = Student("Sanika","8.8")
# stu2 = Student("Shruti","9.2")
# print(stu1.name , stu1.cgpa)


# #self parameter -> self means we are taking about that objects
# class Student:
#     def __init__(self, name, cgpa): #instance attributes
#         self.name = name
#         self.cgpa = cgpa

#     def get_cgpa(self): 
#         return self.cgpa
    
# stu1 = Student("Sanika", 8.8)

# print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")


# #types
# #1) default -> only one parametere which is self
# #2) parameterized -> more tham self parameteres

# class Student:
#     def __init__(self):  #default
#         print("constructor is created..")

#     # def __init__(self, name, cgpa):  #parameterized
#     #     self.name = name
#     #     self.cgpa = cgpa

# stu1 = Student()

# # python does not allow to write two constructor in one class so last constructor will run

