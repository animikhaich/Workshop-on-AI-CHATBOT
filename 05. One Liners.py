# Form a list of numbers (Long method)
test = []
for i in range(10):
    print(test.append(i))
print(test)

# Form a list of numbers (one liner)
test2 = [i for i in range(10)]
print(test2)


text = ['Animikh', 'Akhilesh', 'Akshay', 'Aishwarya', 'Akshaya', 'Harshitha']

# Form a list of strings, convert to lower (Long Method)
lower_list = []
for i in text:
    lower_list.append(i.lower())

print(lower_list)

# Form a list of strings, convert to lower (one liner)
lower_list_2 = [i.lower() for i in text]
print(lower_list_2)

# PYTHON LIST COMPREHENSION
pow2 = [2**x for x in range(10)]
print(pow2)
pow5 = [5**x for x in range(5)]
print(pow5)

# Nested For loops
new_str_long = []
for x in ['Python', 'C']:
    for y in [' Programming', ' Language']:
        new_str_long.append(x+y)
print(new_str_long)

# Nested For loops in 1 line
new_str = [x+y for x in ['Python', 'C'] for y in [' Programming', ' Language']]
print(new_str)


def odd_even(l):
    return sum([1 for k in l if k % 2 == 0])


a = odd_even([1,2,3,4,5])
print(a)