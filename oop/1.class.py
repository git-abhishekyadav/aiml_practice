'''
    The Object is linked to the real life objects
    like teacher and student 

    if there's 3k - 4k student data we cannot redefine parameters for each of them
    so OOP solves this problem by class and object

    In factory where class is blueprint where how to manufacture is defined 

    and the product manufactured is Object  

    and the object takes the memory and not the blueprint i.e class

    object is instance of class
    class is blueprint of object
'''


class Student:
    subject = 'Python'

stu1 = Student()

print(stu1.subject)


'''
    class is blueprint
        it has properties / attributes
        and behaviour / methods
'''

print(type(stu1))
lis1 = [34,34,23]
print(type(lis1))

#we were creating the objects from the class lists, set, tup we were using the methods in those class


#Constructor

class Teacher:
    subject = 'Python'

    #contructor to initialize our object, set the values
    # it is called every time the object is created
    # self is compulsory parameter
    # self is a reference to the current instance of the class.
    # self is automatically passed


    #two types of constructor
    # default 
    # parameterized


    ''' only one contructor is supported so the last one is valid contructor '''

    def __init__(self): 
        print('this is default constructor')


    def __init__(self, name, marks): #teacher1 -> self is reference to teacher1 object
        print('this is parameterized constructor')
        self.name = name
        self.marks = marks

    def get_marks(self):
        return self.marks

teacher1 = Teacher("Abhishek", 98)

print(teacher1.name, teacher1.marks, teacher1.get_marks())

'''
 ATTRIBUTES

    CLASS attributes belong to class common for all

    OBJECT attributes belong to object unique to it
'''

# If class and object both have same attribute then the object attribute has high priority


class Area:
    PI = 3.1
    gravity = 9.8

    def __init__(self):
        self.PI = 3.14

circle = Area()
print(circle.PI)  #3.14
print(circle.gravity)
print(Area.PI)




'''
    METHODS

    instance                    class                   static
1.  1st param self              1st param cls           no compulsory param
    compulsory                                              self or cls 

2.  class and instance          only class attr         no instance or class attr
    attribute                   not instance attr

3.                              @classmethod            @staticmethod
                                    decorator               decorator

'''

class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage
    
    def get_info(self):          #compulsory self for instance method
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}") 

#decorator is function which takes another function and changes its behavior, 
# and how it changed the behavior, by making the function as class method
    @classmethod                     
    def get_storage_type(cls):
        return cls.storage_type

# A @staticmethod does belong to the class. 
# It just doesn't need access to the class (cls) or an instance (self).
# then why create such func and why not create normal method,
#  because logically it belong to that class logic
    @staticmethod
    def calc_discount(price, discount):
        # return price - (discount * price /100)
        print(f"The final amount is {price - (discount * price /100)}")
    
l1 = Laptop("16gb","256gb")
# l1.get_info()
# print(l1.get_storage_type())

l1.calc_discount(40_000, 10)



'''
PRODUCT store
 
 Design & create an online store for Products (name , price)
 Track total products being created
 create a static method to calculate discount on each product based on a % parameter
'''

class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1      
        # self.count += 1         #this creates another variable in that instance

    def get_info(self):            #instance method
        print(f"The price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_product_count(cls):
        print(f"the count of product is {cls.count}")


    @staticmethod
    def calc_discount(price, discount):
        print(f"final price = {price - (price * discount / 100) }")

p1 = Product("pendrive 256gb",10_000)
p2 = Product("mac mini",90_000)
p3 = Product("phone",32_000)


p1.get_info()
p1.calc_discount(p1.price, 12)

# p2.get_product_count()
Product.get_product_count()
