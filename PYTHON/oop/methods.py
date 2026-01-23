# #1) instance ->1st para is self
# #2) class
# #3) static

# #eg 1)Instance methode -> we can access instance as wll as class attributes
# class Laptop:
#     storage_type = "ssd"

#     def __init__(sel, RAM, storage):
#         sel.RAM = RAM
#         sel.storage = storage

#     def get_info(sel): #instance methode
#         print(f"laptop has {sel.RAM} RAM & {sel.storage} Storage {sel.storage_type}")

# l1 = Laptop("16gb", "512gb")
# l2 = Laptop("8gb", "256gb")

# l1.get_info()


# #2) class methode
# # 1st parametere is cls (class)
# #only can access class attributes not instance one
# #decorator -> @classmethod
# #class methode can only access class attributes

# class Laptop:
#     storage_type = "ssd"

#     @classmethod
#     def get_storage_type(cls): #to access class properties
#         print(f"storage type = {cls.storage_type}")

# l1 = Laptop()

# Laptop.get_storage_type()
# l1.get_storage_type() #also with obj name we can access class attributes



# #3)static methods
# #no compulsory parametere -> no self & cls parametere
# # cannot access instance methode and cls method
# #@staticmethod
# #logically they lineup with class
# #eg:

# class Laptop:

#     @staticmethod
#     def calc_discount(price,discont):
#         final_price = price - (discont * price / 100)
#         print(f"discountes price = {final_price}")

# l1 = Laptop()

# l1.calc_discount(40_000, 10)



# #PRACTICE PROBLEM
# #online store with name and price
# class Store:

# #creating a constructor
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def get_info(self):
#         print(f"Price of {self.name} is {self.price}")

# p1 = Store("phone", 10_000)
# p2 = Store("Laptop", 80_000)

# p1.get_info()



#  track total products being created
class Store:
    count = 0
#creating a constructor
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Store.count += 1
        #self.count = += 1 not writing in this way as 

    # def get_info(self): #instance methode
    #     print(f"Price of {self.name} is {self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total products in company are {cls.count}")

p1 = Store("phone", 10_000)
p2 = Store("Laptop", 80_000)
p3 = Store("phone", 10_000)
p4 = Store("Laptop", 80_000)

Store.get_count()

# create static methode to cal discount on each product based on a % parametere
class Store:
    count = 0
#creating a constructor
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Store.count += 1
        #self.count = += 1 not writing in this way as 

    def get_info(self): #instance methode
        print(f"Price of {self.name} is {self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total products in company are {cls.count}")

    @staticmethod
    def calc_discount(price, percentage):
        print(f"Final discounted price = {price -(price * percentage)/ 100}")

p1 = Store("phone", 10_000)
p2 = Store("Laptop", 80_000)
p3 = Store("phone", 10_000)
p4 = Store("Laptop", 80_000)

p1.calc_discount(10_000, 12)