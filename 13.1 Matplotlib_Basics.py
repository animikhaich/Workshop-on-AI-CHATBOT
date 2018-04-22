# =============================================================================
#Simple Line graph using matplotlib
import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [5, 7, 4]
plt.plot(x, y)
plt.show()
# =============================================================================

# =============================================================================
#Adding Colors and labels and index
import matplotlib.pyplot as plt
x1 = [1, 2, 3, 4]
y1 = [5, 6, 7, 8]
x2 = [11, 12, 13, 14]
y2 = [15, 16, 17, 18]
plt.plot(x1, y1, label="first line")
plt.plot(x2, y2, label="second line")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Matplotlib Demo")
plt.legend()
plt.show()
# =============================================================================

# =============================================================================
#Bar charts
import matplotlib.pyplot as plt
x1 = [1, 2, 3, 4]
y1 = [5, 6, 7, 8]
x2 = [11, 12, 1, 5]
y2 = [10, 5, 6, 7]
plt.bar(x1, y1, label="Bars1", color="blue")
plt.bar(x2, y2, label="Bars2", color="red")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Demo of bar chart')
plt.legend()
plt.show()
# =============================================================================

# =============================================================================
# Histograms
import matplotlib.pyplot as plt
population_ages = [11, 22, 53, 64, 77, 85, 110, 23, 75, 9, 100]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
plt.hist(population_ages, bins, histtype="bar", rwidth=0.8)
""" Bins is used for giving the range  """
""" Histogram plots the frequency occuring between that rnage """
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Demo of Histogram')
plt.show()
# =============================================================================

# =============================================================================
# Scatter Plot
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
plt.scatter(x, y, color="blue", marker='*', s=100)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Demo of scatter plot')
plt.show()
# =============================================================================

# =============================================================================
# stack plots
import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
playing = [8, 5, 7, 8, 13]
plt.stackplot(days, sleeping, eating, playing, colors=["black", "blue", "green"])
plt.plot([], [], color="black", label="sleeping")
plt.plot([], [], color="blue", label="eating")
plt.plot([], [], color="green", label="playing")
""" We cannot create lables using stack plot so the above 3 lines of code """
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Demo of stack plot')
plt.legend()
plt.show()
# =============================================================================

# =============================================================================
# Pie-Chart
import matplotlib.pyplot as plt
slices = [2, 1, 1]
""" Slices is used it to indicates the size of the wedges """
activities = ["sleeping", "eating", "playing"]
col = ['b', 'g', 'r']
plt.pie(slices, labels=activities, colors=col, autopct='%1.1f%%')
""" autopct is used for calculating the percentage directly """
plt.title('Demo of pie chart')
plt.show()
# =============================================================================

# =============================================================================
# subplot introduction
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
plt.subplot(1, 2, 1)
plt.scatter(x, y, color='b', label="scatter1")
plt.legend()
plt.subplot(1, 2, 2)
plt.scatter(y, x, color='r', label="scatter2")
plt.legend()
plt.show()
# =============================================================================
