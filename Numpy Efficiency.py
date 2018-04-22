import numpy as np
import time
import sys

# Compute the size of all elements using Lists
l = range(1000)
print("Python Lists, Size:", sys.getsizeof(100)*len(l))

# Compute the size of all elements using numpy
array = np.arange(1000)
print("Numpy, Size:", array.size*array.itemsize)

# ==========================================================

size = 1000000

l1 = range(size)
l2 = range(size)

a1 = np.arange(size)
a2 = np.arange(size)

# Time For Python lists
start1 = time.time()
res1 = [(x+y) for x, y in zip(l1, l2)]
print("\nPython Lists, Time (in ms):", (time.time() - start1)*1000)

# Time For Python lists
start2 = time.time()
res2 = a1 + a2
print("Numpy, Time (in ms):", (time.time() - start2)*1000)
