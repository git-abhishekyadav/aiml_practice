'''
    Encapsulation
    Abstraction
    Inheritance
    Polymorphism
'''

# 1.Encapsulation
#     Wrapping data & function in single unit
#         data + methods = class


#     data hiding
#         public attr     -> accessible inside and outside class
#         protected attr  -> class and sub class (inherited clss)
#         private attr    -> accessible only inside class

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self._balance = balance     #protected
        self.__balance = balance    #private  -> data mangling

acc1 = BankAccount("John Doe", 10_000)

# protected 
# just convention and not enforced
# but we can access it 
print(acc1.name, acc1._balance)
print(acc1.__balance)       # we can't acces the private ones

# if we need to access 
    # access it by getters and setters
