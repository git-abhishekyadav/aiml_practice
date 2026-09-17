'''
    POLYMORPHISM 
    many forms

    multiple func having same name but different forms i.e implementation
'''


# operator overloading

#              +
#             / \
#            /   \
#         add      concatenate


# 1.Function overriding

    # (inheritance) redefining parent class func in child class

class Employee:

    def get_designation(self):
        print("designation = Employee")

class Teacher(Employee):

    def get_designation(self):
        print("designation = Teacher")

t1 = Teacher()
t1.get_designation()        # the child method override the parent method

# Inheritance → child gets the parent's methods.
# Overriding → child provides its own implementation of an inherited method.


# 2.Duck Typing

# "If it walks like a duck and quacks like a duck, then treat it like a duck."

class Teacher:

    def get_designation(self):
        print("designation = Teacher")

class Accountant:

    def get_designation(self):
        print("designation = Accountant")

t1 = Teacher()
t1.get_designation()

t2 =  Accountant()
t2.get_designation()
# Same method/functionality + unrelated classes + Python uses the object's available behavior = Duck Typing.