import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.linear_model import LinearRegression

print(style.available)
style.use('dark_background')

# Open the file and load data
with open('Database/mpg.csv', 'r') as file:
    data_set = file.read().split('\n')[1:-1]

# Taking the input (X) as Weight
# Taking the output (y) as MPG
X = np.array([[float(i.split(',')[4]) for i in data_set]]).T
y = np.array([[float(i.split(',')[0]) for i in data_set]]).T

LR = LinearRegression()
LR.fit(X, y)

plt.plot(X, LR.predict(X), c='r')
plt.scatter(X, y, marker='x', c='b')
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.title('ANN Regression on 1D MPG Data')
plt.show()
