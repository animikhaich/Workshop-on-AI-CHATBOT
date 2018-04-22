# Python Flow Control

# If Statement
num = int(input('Enter the Number:'))
if num == 0:
    print(num, 'is Zero')
elif num > 0:
    print(num, 'is a positive Number')
else:
    print(num, 'is a negative number')
print('This is always printed')

# nested if-else
num = int(input('Enter the Number:'))
if num >= 0:
    if num == 0:
        print(num, 'is Zero')
    else:
        print(num, 'is a positive Number')
else:
    print(num, 'is a negative number')
print('This is always printed')



# FUNCTIONS:

# empty function in python
def fun():
    pass


# function without return value
def func():
    print("hello")


func()
func()
func()


# function with return value
def func1():
    return "hello!"


print(func1())


# A Simple Python program to demonstrate working
# of yield

# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)


# Function with default argument
def say(message, times=1):
    print(message * times)


say('hello')
say('world', 5)


# Function with a keyword
def funct(a, b=5, c=10):
    print('a is', a, 'b is', b, 'c is', c)


funct(3, 5)
funct(25, c=25)
funct(c=50, a=10)


# A Python program to demonstrate that a function
# can be defined inside another function and a
# function can be passed as parameter.

# Adds a welcome message to the string
def messageWithWelcome(str):
    # Nested function
    def addWelcome():
        return "Welcome to "

    # Return concatenation of addWelcome()
    # and str.
    return addWelcome() + str


# To get site name to which welcome is added
def site(site_name):
    return site_name


print(messageWithWelcome(site("AI WORKSHOP")))

''' Program make a simple calculator that can add, subtract, multiply and divide using functions '''


# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user
choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")


# args and kwargs
def add(*args):
    print(args)


add(1, 2, 3, 4)


def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)


multiply(4, 5)
multiply(2, 3, 4)
multiply(3, 5, 10, 6)


def sum(**kwargs):
    print(kwargs)


sum(name='abc', rollno='85', age='20')


def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))


print_values(
    name_1="Alex",
    name_2="Gray",
    name_3="Harper",
    name_4="Phoenix",
    name_5="Remy",
    name_6="Val"
)



# LAMBDA FUNCTIONS


# Python code to illustrate cube of a number
# showing difference between def() and lambda().


def cube(y):
    return y * y * y;


g = lambda x: x * x * x
print(g(7))

print(cube(5))

# Python code to illustrate
# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)

# Python code to illustrate
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x * 2, li))
print(final_list)


