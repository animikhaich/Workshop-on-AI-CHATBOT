import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
from matplotlib import style

# print(style.available)
style.use('bmh')


# The linear regression algorithm
def linear_regression(xs, ys):
    slope = ((mean(xs) * mean(ys) - mean(xs * ys)) /
             ((mean(xs))**2 - mean(xs**2)))
    intercept = mean(ys) - slope * mean(xs)
    return slope, intercept


# Open the file and load data
with open('Database/mpg.csv', 'r') as file:
    data_set = file.read().split('\n')[1:-1]

# Taking the input (X) as Weight
# Taking the output (y) as MPG
X = np.array([float(i.split(',')[4]) for i in data_set])
y = np.array([float(i.split(',')[0]) for i in data_set])

# Use the linear regression algorithm to compute slope and intercept
m, c = linear_regression(X, y)

# Calculate y for each x w.r.t. slope and intercept
regression_line = np.array([m * x + c for x in X])

# Plot the data
plt.scatter(X, y, marker='x', c='b')
plt.plot(X, regression_line, c='r')
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.title('ANN Regression on 1D MPG Data')
plt.show()
