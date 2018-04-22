# A Python program to demonstrate that we can store
# large numbers in Python
x = 10000000000000000000000000000000000000000000
x = x + 1
print(x)
# A Python program to show that there are two types in
# Python 2.7 : int and long int
# And in Python 3 there is only one type : int
print(type(x))
print(100 ** 100)

# User Input
print('Hey! Enter some text: ')
x = input()
print('Text entered is: ', x)
print('Type:', type(x))

# print and user Input
print("Hello!")
x = input("Hi! Tell me your name: ")
print("Hi, nice to meet you,", x)
y = input("What is your email? :")
print("Oh! Your email ID is:", y)
z = input("What is your Phone Number? :")
print("Oh! Your Phone Number is:", z)

# Important Concepts
print("A\nB\nC\nD")
print("A\tB\tD")
print("WXY\bZE")

# Multi-line Statements
import sys
first_one = 'I'
second_one = 'love'
third_one = 'Python'
final_one = first_one + \
    second_one + \
    third_one
sys.stdout.write('\n'+final_one)


# Single double and tripe Quotes
print('This is in Single Quotes, It is taken as string')
print('Application for single quotes is when we have a Double quote inside the String: ')
print("This is in Double Quotes, It is also taken as a string")
print("Application for double quotes is when we have a single quote inside the String: That's awesome!")
print('''This is 3 single quotes together
This prints Multi-line Statements
This is working pretty well!''')


# Multiple line program in a single line
v = '\n\n'
print(v+"The following is a single line execution of the entire thing, but is not recommended by PEP 8")
import sys; p = "Let's do Python Together!"; sys.stdout.write(p+'\n\n'+p+v+p+v)

# ADD integers
print('Enter integer 1: ')
x = input()
print('Enter integer 2: ')
y = input()
num1 = int(x)
num2 = int(y)
print(num1, '+', num2, '=', num1+num2)

Shorter way of the same program
x, y = int(input("Num1: ")), int(input("Num2: "))
print(x, '+', y, '=', x+y)

# Floor and Modulus
import math
x, y = 137, 456
print('This is raw Division', y/x)
print('This is the floor Operator:', math.floor(y/x))
print('This is the ceil Operator:', math.ceil(y/x))
print('This is the round Operator:', round(y/x))
print('This is the modulus Operator:', abs(3+4j))

# Assigning values to variables
x = 100
v = ' \n'
y = 300
c = 'I am happy'
print('x+y:', x+y)
print(v+c)

# Multiple Assignment
x = y = z = 100
print(x)
print(y)
print(z)
a, b, c = 100, 200, '\nI love RNSIT'
print(a, b, c)


# Exchange 2 Variables
print("This is the Beauty of Python!")
a = 2
b = 3
print("Before Exchange: ", end="")
print("a =", a, "| b =", b)
b, a = a, b
print("After Exchange: ", end="")
print("a =", a, "| b =", b)


# Any and All Functions. Similar to OR and AND gate
all_true = [True, True, True, True]
all_false = [False, False, False, False]
mixed = [True, False, True, True]
# Any operator returns True if any one of the Items are true (OR Gate)
print("All True | Any Operator:", any(all_true))
print("All False | Any Operator:", any(all_false))
print("All Mixed | Any Operator:", any(mixed))
# All operator returns True if All of the Items are true (AND Gate)
print("All True | All Operator:", all(all_true))
print("All False | All Operator:", all(all_false))
print("All Mixed | All Operator:", all(mixed))

# Increment and Decrement Operator
# There is no Increment and Decrement operator in Python
# i++ and i-- or ++i and --i does NOT work in Python
i = 10
print('Initial Value:', i)
print('Incrementing i')
i += 1
print('After Increment:', i)
i -= 2
print('After Decrement:', i)
