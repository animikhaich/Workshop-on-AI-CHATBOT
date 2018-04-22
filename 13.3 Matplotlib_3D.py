#3D plot
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure() # Creating the figure window
ax1 = fig.add_subplot(1,1,1, projection = '3d') #Telling the intereeter to work on 3dimensions
x =np.array( [[1,2,3,4,5],[6,7,8,9,10]])
y = np.array([[2,4,5,6,7],[8,2,3,4,5]])
z = np.array([[1,3,2,5,8],[6,9,7,3,4]])
ax1.plot_wireframe(x,y,z) #wire-frame takes only 2-D numpy arrays as arguments
ax1.set_xlabel("x-axis")
ax1.set_ylabel("y-axis")
ax1.set_zlabel("z-axis")
plt.show()

#3D sctter plot
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure() # Creating the figure window
ax1 = fig.add_subplot(1,1,1, projection = '3d') #Telling the intereeter to work on 3dimensions
x =np.array( [[1,2,3,4,5],[6,7,8,9,10]])
y = np.array([[2,4,5,6,7],[8,2,3,4,5]])
z = np.array([[1,3,2,5,8],[6,9,7,3,4]])
ax1.scatter(x,y,z,marker="*", color="blue", s=100)
x1=np.array( [[-1,-2,-3,-4,-5],[-6,-7,-8,-9,-10]])
y1= np.array([[-2,-4,-5,-6,-7],[-8,-2,-3,-4,-5]])
z1 = np.array([[1,3,2,5,8],[6,9,7,3,4]])
ax1.scatter(x1,y1,z1,marker ="+",color = "red", s=50)
ax1.set_xlabel("x-axis")
ax1.set_ylabel("y-axis")
ax1.set_zlabel("z-axis")
plt.show()

#intro to 3D plane
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1, projection='3d')
x,y,z = axes3d.get_test_data() #it generates test data of type nd array and through these points 
#wireframe routes the wire
print(x)
print(y)
print(z)
ax1.plot_wireframe(x,y,z,rstride = 5, cstride=5)
ax1.set_xlabel("x-axis")
ax1.set_ylabel("y-axis")
ax1.set_zlabel("z-axis")
plt.show()

# 3D wire frame plot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import time

def generate(X, Y, phi):
    # Generates Z data for the points in the X,Y mesh-grid and parameter phi
    R = 1-np.sqrt(X**2+Y**2)
    return np.cos(2*np.pi*X+phi)*R


fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
# make the X, Y meshgrid
xs = np.linspace(-1, 1, 50)
ys = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(xs, ys)
# Set the z axis limits so they aren't recalculated each frame
ax.set_zlim(-1,1)
# begin plotting
wframe = None
for phi in np.linspace(0,180. / np.pi, 100):
    # If a line collection is already remove it before drawing
    if wframe:
        ax.collections.remove(wframe)
    # plot the new wireframe and pause briefly because contineous
    Z = generate(X, Y, phi)
    wframe = ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1)
    plt.pause(.001)