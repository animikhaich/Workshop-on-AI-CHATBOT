import matplotlib.pyplot as plt
import math

Pi = 3.14159625
fig, ax = plt.subplots()
'''creates a figure as well as subplot'''
'''here ax is the subplot variable'''
x = []
y = []


def points_in_circum(r, n=20):
    circle = [(math.cos(2*Pi/n*x)*r, math.sin(2*Pi/n*x)*r) for x in range(0, n+1)]
    return circle
circle_list = points_in_circum(3,50)
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
for t in circle_list:
    
    x.append(t[0])
    y.append(t[1])
    plt.plot(x,y,"o--")
    plt.pause(0.1)
plt.show()

# Plot Time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime

# create date
y = [2, 4, 6, 8, 10, 21, 14, 5, 18, 20]
x = [datetime.datetime.now()+datetime.timedelta(hours=i) for i in range(len(y))]
# plot
plt.plot(x, y)
plt.gcf().autofmt_xdate() #right align
plt.show()

