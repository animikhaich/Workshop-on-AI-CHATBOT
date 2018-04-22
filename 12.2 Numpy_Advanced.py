import numpy as np

c = np.array( [[[  0,  1,  2],               # a 3D array (two stacked 2D arrays)
                [ 10, 12, 13]],
               [[100,101,102],
                [110,112,113]]])

print('New 3D array c:\n', c)

print('Find the shape of C: ', c.shape)

print('Same as c[1,:,:] or c[1]:\n', c[1, :, :])

print('Same as c[:,:,2]:\n', c[:, :, 2])

print('Return a Flattened array: ', c.ravel())


a = np.floor(10*np.random.random((2,2)))
print('New Array:\n ', a)

b = np.floor(10*np.random.random((2,2)))
print('New Array:\n ', b)

c = np.vstack((a,b))
d = np.hstack((a,b))

print('Horizontal stacking of a & b: \n', d)
print('Vertical stacking of a & b: \n', c)

# Splitting Arrays
print('Splitting Arrays:')
a = np.floor(10*np.random.random((2,12)))

print('New Array:\n', a)

print('Split into 3 seperate arrays: \n',np.hsplit(a,3))   # Split a into 3

# Dot product
import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[11, 12], [13, 14]])
print(np.dot(a, b))

# Inner product of 1D Inner array
import numpy as np
print(np.inner(np.array([1, 2, 3]),  np.array([0, 1, 0])))  # Equates to 1*0+2*1+3*0
print(np.inner(np.array([[1, 2, 3], [2, 3, 4]]),  np.array([[0, 1, 0], [2, 3, 4]])))  # Equates to 1*0+2*1+3*0

# Multi Dimensional array example
import numpy as np
a = np.array([[1, 2], [3, 4]])
print('Array a:')
print(a)
b = np.array([[11, 12], [13, 14]])
print('Array b:')
print(b)
print('Inner Product:')
print(np.inner(a, b))
# 1*11+2*12,  1*13+2*14
# 3*11+4*12,  3*13+4*14

# Matrix Multiplication
# For 2D array,  it is a matrix multiplication
import numpy as np
a = np.array([[1, 0], [0, 1]])
b = np.array([[4, 1], [2, 2]])
print(np.matmul(a, b))

# Determinants for matrix input
import numpy as np
a = np.array([[1, 2], [3, 4]])
print(np.linalg.det(a))
b = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
print(b)
print(np.linalg.det(b))
print(6*((-2)*7 - 5*8) - 1*(4*7 - 5*2) + 1*(4*8 - (-2)*2))

# Inverse Matrix Calculation __Part 1
import numpy as np
x = np.array([[1, 2], [3, 4]])
y = np.linalg.inv(x)
print(x)
print(y)
print(np.dot(x, y))     # Identity Matrix


x = np.array([[1, 1], [1, 1]])
y = np.linalg.inv(x)
print(x)
print(y)
print(np.dot(x, y))     # Identity Matrix