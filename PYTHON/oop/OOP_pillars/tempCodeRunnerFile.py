from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod #method whose implementation not done in parent class but done in child class
    def make_sound():
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar!")

lion = Lion()
l