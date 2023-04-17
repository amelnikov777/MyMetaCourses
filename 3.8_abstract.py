from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        print('Animal moves')

class Cat(Animal):
    def move(self):
        super().move()
        print('Cat moves')
        super().move()
        
    def speak(self):
        print('Cat speak')

class Dog(Animal):
    def move(self):
        print('Dog moves')

d = Dog()
d.move()
c = Cat()
c.move()
c.speak()