'''
    ABSTRACTION
    Hiding internal details & showing only essential features

    abstract class => blueprint for other classes


    Most confusing interview question
    difference between data hiding and abstraction
'''


#ABC -> Abstraction based classes
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass            #no implement so pass keyword
                # pass represent null value, no task perform


class Lion(Animal):

    def make_sound(self):
        print("Roar")

class Cow(Animal):

    def make_sound(self):
        print("Moo")

lion = Lion()
lion.make_sound()

cow = Cow()
cow.make_sound()