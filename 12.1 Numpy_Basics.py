## NUMPY BASICS
import numpy as np
# Declare a Numpy Array
print('Declaration of the array: ')
array = np.array([[1, 2, 3, 4], [5, 2, 2, 3], [7, 3, 9, 1]])
print(array)

# Finding Out the Item size of each Item of the array
print('Size of each item of the array: ', end='')
item_size = array.itemsize
print(item_size)

print('Shape of Array: ', array.shape)

# Resizing the Array
print('Reshaped Array: ')
array = array.reshape(6, 2)
print(array)

# Using dtype argument
print('Redeclaring the same array with float64 dtype. float64 takes 8 bytes of space: ')
array = np.array ([[1, 2, 3, 4], [5, 2, 2, 3], [7, 3, 9, 1]], dtype='float64')
print(array)
print('Item size: ', array.itemsize)

# An empty array
empty_array = np.empty((2, 3))      # Always takes tuples
print('Empty Array: \n', empty_array)

# Ones and Zeros
print('Ones: \n', np.ones((2, 3), dtype = 'int'))
print('zeros: \n', np.zeros((2, 3)))

# Transpose
print('Transpose of the array:\n ', array.transpose())
print('Alternative way:\n ', array.T)

# Range
array = np.arange(10, 50, 3)
print('Range of array b/w 10 and 50 in steps of 3:\n',array)

# Random
array = np.random.randn(2,3)
print('Random numbers 2,3 array:\n',array)

# Array Operations
a = np.array([10, 20, 30, 40, 50])
b = np.arange(1,6)

print('Array a:', a)
print('Array b:', b)

c = a - b
print('The array subtraction is: ', c)

c = a + b
print('The array Addition is: ', c)

c = a * b
print('The array Miltiplication is: ', c)

c = a + 50
print('The array Addition with scalar is: ', c)

c = a / b
print('The array Division is: ', c)

c = b**5
print('b raised to the power 5: ', c)

c = a < 40
print('Array boolean comparison: ', c)

c = a.dot(b)
print('Finding the dot product: ', c)

c = np.dot(a,b)
print('Alternative method for dot product: ', c)

c = np.sqrt(a)
print('Square Root of array a:', c)


# Intermediate
def f(x, y):
    return 10*x+y


b = np.fromfunction(f, (5, 4), dtype=int)

print('New array declared from function:\n', b)

print('Element 2,3 of b: ', b[2,3])

print('Each row in the second column of b: ', b[0:5,1])

print('Equivalent to the previous example: ',b[:,1] )

print('Each column in the second and third row of b:\n', b[1:3,:])

print('Last row from bottom: ', b[-1])
