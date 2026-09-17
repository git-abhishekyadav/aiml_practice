'''
    INHERITANCE

    Reusing  attr & methods from a parent (base) class

    to Child (Derived) class

'''

# 1 Single Level Inheritance
        # Parent Class
        #      ↓
        # Child Class

class Employee:
    start_time = "10am"
    end_time = "7pm"

    def change_end_time(self, new_end_time):
        self.end_time = new_end_time 

class Developer(Employee):
    def __init__(self, task):
        self.task = task

class Accounts(Employee):
    def __init__(self, role):
        self.role = role

    '''
    Here comes the data hiding 
    protected and private 
    where protected attr are accessible in sub class
    and private attr are not in sub class
    '''


staff1 = Accounts("HR")
staff1.change_end_time("6pm")
print(staff1.role, staff1.start_time, staff1.end_time)

staff2 = Developer("Research & Develop")
print(staff2.task, staff2.start_time, staff2.end_time)


# 2. Multi level inheritance

        # Grandparent
        #     ↓
        #   Parent
        #     ↓
        #   Child

class Employee:
    start_time = "10am"
    end_time = "6pm"

    def work(self):
        print("Employee is working")

class Manager(Employee):

    def __init__(self, assign_task):
        self.assign_task = assign_task

    def manage_team(self):
        print("Manager is managing the team")

class SeniorManager(Manager):

    def __init__(self, assign_role, assign_task):
        super().__init__(assign_task)
        self.assign_role = assign_role

    def make_strategy(self):
        print("Senior Manager is making strategy")


employee = SeniorManager("Dev", "mongodb_query")

employee.work()           # Employee
employee.manage_team()    # Manager
employee.make_strategy()  # SeniorManager
# print(employee.assign_role,employee.assign_task)
emp2 = Manager("AI_ML")
print( emp2.assign_task)    # cannot assign role


# 3. Multiple inheritance

# Parent 1 ──┐
#             ↓
#          Child
#             ↑
# Parent 2 ──┘

class Teacher:

    def __init__(self, salary):
        self.salary = salary


class Student:

    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher, Student);
    
    def __init__(self, salary, gpa, name):
        super().__init__(salary)        
        Student.__init__(self, gpa)     #when calling by class name need to pass self not in super
        self.name = name

ta1 = TA(15_000, 9.3, "John")

    

