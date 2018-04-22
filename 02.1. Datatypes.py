# BASIC CONCEPTS OF list_1S

noprimes=[j for i in range(2, 8) for j in range(i*2, 50, i)]
print(noprimes)
#-----------------------------------------------
# list_1 which extracts number

string = "my phone number is : 11122 !!"
print("\nExtracted digits")
numbers = [x for x in string if x.isdigit()]
print(numbers)

#other way of creating and updating the list_1s

print("\nExtracted digits")
numbers=[]
for x in string :
    if x.isdigit():
        numbers.append(x)

print(numbers)
# -------------------------------------------------

# A list_1 of list_1 for multiplication table

a = 5
table = [[a, b, a * b] for b in range(1, 11)]

print("\nMultiplication Table")
for i in table:
    print(i)

table=[]
for b in range(1,11):
    individual=[a,b,a*b]
    table.append(individual)

print(table)
# --------------------------------------------------
# deleting an item from the list_1
list_1=[1,2,3,4]
del list_1[2]
print(list_1)


# BASIC list_1 OPERATIONS

# Python Expression        |                        Results	   |       Description
# -----------------------------------------------------------------------------------
# len([1, 2, 3])	     	 |                             3	   |            Length
# [1, 2, 3] + [4, 5, 6]  	 |	          [1, 2, 3, 4, 5, 6]	   |      Concatenation
# ['Hi!'] * 4              |  ['Hi!', 'Hi!', 'Hi!', 'Hi!']	   |         Repetition
# 3 in [1, 2, 3]	         |                           True	   |         Membership
#
# similar to  [1, 2, 3] + [4, 5, 6]
# list_1=[1,2,3]
# list_1.extend([4,5,6])
# print(list_1)
# -------------------------------------------------

# SLICING

lst=list(range(0,10))
print(lst)
lst1_ = lst[1:]
print(lst1_)
#
lst1_ = lst[1:9] #-----runs till one item before the specified last index
print(lst1_)

lst1_ = lst[1:9:2]#---runs from 1 to 11 with a step of 2
print(lst1_)

lst1_ = lst[9::-2]
print(lst1_)

lst1_ = lst[::-1]
print(lst1_)

# OTHER DATA TYPES:

# 2. TUPLES

# TUPLES ARE SIMILAR TO list_1S WITH THE ONLY DISCRIMINATION THAT list_1S ARE MUTABLE ,BUT TUPLES
# ARE IMMUTABLE
# THEY ARE REPRESENTED AS FOLLOWS ( , )
# EXAMPLE:

a=(2,3,4,5,6)

# ACCESSING THE TUPLE ELEMENTS

print(a[0],a[1])
print(a)
# a[0]=2  # THROWS AN ERROR BCOZ TUPLES ARE IMMUTABLE

# 3.SETS

# SET IS AN UNORDERED COLLECTION OF DATA ITEMS
# IT BASICALLY AVOIDS REPETITION.
# THEY ARE REPRESENTED BY {}
# FOR EX:-

a = {1,1,2,2,2,3,3,3,3}
print(a)
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)
b = {1.0 , 1 , (1,2)}
print(b)

#  4.DICTIONARY

# TO UNDERSTAND THIS DATATYPE LET US MAP IT WITH THE NORMAL ENGLISH DICTIONARY WHICH HAS
# THE WORDS AND THEIR MEANINGS......
# SIMILARLY IN THIS DATA TYPE WE REPRESENT THE ITEMS AS FOLLOWS
# {KEY:VALUE}

b = {'name':'Akhilesh','usn':'12'}
# HERE 'name' and 'usn' ARE CALLED KEYS AND 'Akhilesh' and '12' ARE CALLED VALUES
print(b)

# ACCESSING DICTIONARY ELEMENTS

# SYNTAX: VALUE=VAR[KEY]

c = b['name']
d = b['usn']
print(c,d)

# IT SUPPORTS ASSIGNMENT

b['name']='Akhil'
print(b)

# TO MODIFY THE KEY

# SYNTAX:

# dictionary[new_key] = dictionary[old_key]
# del dictionary[old_key]
b['roll no']=b['usn']
print(b)
del b['usn']
print(b)
