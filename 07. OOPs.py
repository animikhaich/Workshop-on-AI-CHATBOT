# Simple class example
class myClass:
    def fun(self):   # Simple method
        print('hello world')


obj=myClass()  # Syntax for creating objects
obj.fun()      # Accessing method with the help of dot operator


# __init__method
class test():

    def __init__(self, name):   # Init method is taking parameter name along with usual self
        self.identity = name

    def say_hi(self):
        print('Hello, my name is ', self.identity)


obj = test('Aishwarya')   # Creating object with the help of class name along with the parameters
obj.say_hi()


#  class variables and instance variables
#  program to show difference between class variables and instance(object) variables
#  program to print usn and branch of the student
class ECEStudents:
    stream = 'ECE'  # class variable

    def __init__(self,usn):
        self.usn=usn
# objects of class ECEStudents


a = ECEStudents('1RN15EC009')
b = ECEStudents('1RN15EC010')
print(a.stream)  # prints ECE
print(b.stream)  # prints ECE
print(a.usn)     # prints usn pf a
# class variables can be accessed using class name also
print(ECEStudents.stream)  # prints ECE

# python program to define instance variable inside normal method also


class Students:
    stream='ECE'

    def __init__(self, usn):
        self.usn = usn
        self.address = None

    def set_address(self, address):   # instance variable inside normal function
        self.address = address

    def get_address(self):
        return self.address


a = Students('1RN15EC009')
a.set_address('Bangalore, RNSIT')
print(a.get_address())

# INHERITANCE
# new class is created with little modifications of the existing class, this existing class is called as base class
#  and the new class is called as the derived class
'''syntax-
class BaseClass_name:
    body of the base class
class DerivedClass_name(BaseClass_name):
    body of the derived class'''


# program to show inheritance
class Person:      # Person is a base class
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def name(self):
        return self.first_name + " " + self.last_name   # returns the name


class Employee(Person):
    def __init__(self, first, last, staff_num):
        Person.__init__(self, first, last)       # inheriting init method of the persons class is invoked by the init method of employees class
        self.staff_number = staff_num             # staff number is object variable

    def get_employee(self):
        return self.name() + "," + self.staff_number   # inheriting name method from person class to employee class


x = Person("Shahrukh", "Khan")    # x is person class object
y = Employee("Shahrukh", "Khan", "1011")
print(x.name())
print(y.get_employee())


# how to check if a class is subclass of another
# Python provides a function issubclass() that directly tells us if a class is subclass of another class.
class Base(object):    # empty base class
    pass


class Derived(Base):       # empty derived class
    pass


print(issubclass(Derived, Base))    # is derived class subclass of base class? true
print(issubclass(Base, Derived))    # is base class subclass of derived class?false
b = Base()                           # base class object
d = Derived()                        # derived class object
print(isinstance(b, Derived))       # b which is instance of base class is not subclass of derived class
print(isinstance(d, Base))          # d which is instance of derived class is the subclass of base class


# multiple inheritance
# program to show the working of the multiple inheritance

class Base1:
    def __init__(self):
        self.str1 = 'Electronics'


class Base2:
    def __init__(self):
        self.str2 = "Computer Science"


class Derived(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)

    def print_str(self):
        print(self.str1+","+self.str2)


ob = Derived()
ob.print_str()

