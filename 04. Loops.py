# Python Flow Control

'''
while loop
syntax
while(expression):
    statement(s)
'''

# program to find sum up-to n terms
sum = 0     # initialization
i = 0       # initialization
n = int(input('Enter the range: '))  # taking value from the keyboard

while i <= n:
    sum += i                        # adding numbers (equivalent to sum = sum+i)
    i += 1                          # incrementing i
print('the sum is:',sum)


# while-else
counter = 0
while counter <= 4:
    print('inside the loop')
    counter += 1
else:
    print('outside the loop')


# if-else statements
'''syntax-
if(conditon):
    statements
else:
    statements'''

# python program to check if a given number is positive or not using if-else statements
m = int(input('Enter the number: '))
if m == 0:
    print('number is zero')
elif m > 0:
    print('number is positive')
else:
    print('number is negative')


# nested if-else statements
# same program can be written using nested if-else statements
num = int(input('Enter the number: '))
if num > 0:
    if num == 0:
        print('number is zero')
    else:
        print('number is positive')
else:
    print('number is nrgative')


# for loop
'''syntax-
for val in sequence:   # here val is the varaiable thet takes value of each item in sequence on each iterations
    body of for loop
    '''

# program to find the sum of all numbers in the list
sequence = [1, 2, 3, 4]  # list of numbers
sum = 0
for val in sequence:    # for loop
    sum = sum + val     # sum += val
print('sum:',sum)

learn = ['python','machine_learning','deep_learning']
for i in range(len(learn)):  # len(learn) = 3
    print('I will be learning',learn[i])  # syntax for accessing elements of list

# break statements
# The break statement terminates the loop containing it.
#  Control of the program flows to the statement immediately after the body of the loop.
# If break statement is inside a nested loop (loop inside another loop), break will terminate the innermost loop.
# syntax-break
for char in 'RNSIT':
    if char == 'I':
        break
    print(char)
print('the end')


# The continue statement is used to skip the rest of the code inside a loop for the current iteration only.
#  Loop does not terminate but continues on with the next iteration.
for char in 'RNSIT':
    if char == 'I':  # when string is 'I' rest of the block doesnt get executed but continues with next iteration
        continue
    print(char)
print('the end')

# Program to illustrate loop with condition at the bottom
# Roll a dice until the user chooses to exit
import random
input('Press enter to roll the dice: ')
while True:
    num = random.randint(1, 6)  # randint function will give random integers between the range specified
    print('you got', num)
    option = input('Do u want to continue playing?(y/n): ')
    if option == 'n':
        break


