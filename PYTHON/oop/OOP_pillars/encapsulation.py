#wrapping data & functions into single unit
#use in data hiding
#public attributes -> accesable within and out of the class
#protected -> in class also in subclasses
#private -> only inside the class

# class Bankaccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self._balance = balance #protected attributes
#         #in python data hidding is by convenation not inforce
#         # self.__balance = balance # private -> data mangling

# acc1 = Bankaccount("Sanika Jagtap", 40_000)
# print(f"{acc1.name} have {acc1.balance} in Account.")


#to get value of private attributes -> gettesa & setters
class Bankaccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance #private

    def get_balance(self): #getter function
        return self.__balance
    
    def set_balance(self, newBalance):
        self.__balance = newBalance
    
acc1 = Bankaccount("sanika jagtap", 40_000)
acc1.set_balance(45_000)
print(acc1.name , acc1.get_balance())

# we can also access private attributes directly 
print(acc1.name, acc1._Bankaccount__balance)
