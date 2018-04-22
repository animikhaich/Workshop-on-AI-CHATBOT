import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.preprocessing import scale
import numpy as np

style.use('bmh')


# Open the file and load data
with open('Database/mpg.csv', 'r') as file:
    data_set = file.read().split('\n')[1:-1]

# Taking the input (X) as Weight
# Taking the output (y) as MPG
X = np.array([[float(i.split(',')[4]) for i in data_set]]).T
y = np.array([[float(i.split(',')[0]) for i in data_set]]).T
N = X.shape[0]


# with open('Database/height.csv', 'r') as file:
#     data_set = file.read().split('\n')[1:-1]
#
# # Taking the input (X) as Weight
# # Taking the output (y) as MPG
# X = np.array([[float(i.split(',')[1]) for i in data_set]]).T
# y = np.array([[float(i.split(',')[2]) for i in data_set]]).T
# N = X.shape[0]


# Normalizing the Weight
# X = scale(X)
X = (X - np.mean(X)) / np.std(X)

# Appending ones for bias
X = np.hstack((np.ones(N).reshape(N, 1), X))

# Initializing weights
w = np.array([0, 0])

# Number of Epochs and Learning Rate
epoch = 100
lr = 1E-4

# Start training
for i in range(epoch):
    grad = np.array([0., 0.])

    # For each input, training separately
    for j in range(N):
        # Formatting the input and output for the given data
        x_i = X[j, :]
        y_i = y[j][0]

        # Finding the Error
        E = y_i - np.dot(w, x_i)
        grad += x_i * E

    # Updating weights
    w = w + grad * lr

    # Plotting the data. Live plot
    x = np.array([np.min(X[:, 1]), np.max(X[:, 1])])
    bf_line = w[0] + w[1] * x
    if i == 0:
        plt.scatter(X[:, 1], y, marker='x', c='b')
    plot, = plt.plot(x, bf_line, 'r-')
    plt.xlabel('Weight (Normalized)')
    plt.ylabel('MPG')
    plt.title('ANN Regression on 1D MPG Data')
    plt.pause(0.05)
    plot.remove()

plot, = plt.plot(x, bf_line, 'r-')
# plt.pause(10)
plt.show()
