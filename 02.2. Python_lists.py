# Lists in Python
my_list = [0, 2, 10, 'Akhilesh', 3.4]
n_list = ['happy',  [0, [0.5, 4.5, [2, 5, 7], -1, 15], 3]]
y = n_list[1][1][3]
print(y)
x = my_list[3]
print(x)

# Negative Indexing
n_list = ['Happy',  [0, 1, 2, 3]]
y = n_list[1][-3]
print(y)

# Slicing
j_list = ['a', 'i', 'c', 'h']
w = j_list[0:2]
print(w)

# Appending & Extending
j_list.append([6, 5, 8])
print(j_list)
j_list.extend([9, 10, 7, 'hello'])
print(j_list)

# Append_2
o_list = [1, 3, 5]+[2, 4, 6]
print(o_list)

# Append_3
h_list = ['Akku']*5
print(h_list)

# insert
td_list = [1, 10, 15, 20, 90]
td_list.insert(2, 6)        # This number "1" is already there,  Python is Smart and it won't repeat the same number
                            # this means that "INSERT VALUE 6 IN POS 2"
print(td_list)
td_list[2:4] = [5, 8, 7, 9, 7]   # the td_list[2] and td_list[3] will be replaced with [5, 8, 7, 9, 7]
print(td_list)

# next
iy_list = ['z', 'a', 'r', 'k']
del iy_list[2]          # del iy_list[1:2]
print(iy_list)

# Python list Method
my_list = [1, 2, 15, 7, 8]
a = my_list.index(2)
print(a)

# reverse the list
my_list.reverse()       # ----also my_list[::-1]
print(my_list)

# Sort the list
my_list.sort()          # ----default ascending order
print(my_list)
