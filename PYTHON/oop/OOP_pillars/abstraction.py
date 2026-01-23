#hiding internal details & showing only essential features
# to implement we use abstract classes -> abc module (abstract base class)
#which is blueprint for other classes


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod #method whose implementation not done in parent class but done in child class
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar!")

lion = Lion()
lion.make_sound() 