#!/usr/bin/python3.6
# -*coding:utf-8 -*

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Set the environment
"""fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.set_xlim3d(0, 6.28)
ax.set_ylim3d(-1.1,1.1)
ax.set_zlim3d(-1.1, 1.1)"""

# Example 2
"""param = np.linspace(-3.14, 3.14, 100)
u, v = np.meshgrid(param, param)
a, b = 2, 2
X = (a + np.sin(v))*np.cos(u)
Y = (a + np.sin(v))*np.sin(u)
Z = u + np.cos(v)

ax.plot_surface(X, Y, Z, color = 'r', alpha = 0.3, rstride = 2, cstride = 2)

	# Display curve u = 0
u = 0
v = np.linspace(0, 6.3, 50)
X = 2 + np.sin(v)
Y = 0 * v 
Z = np.cos(v)
ax.plot(X, Y, Z, color='b')

	# Display curve v = 0
v = 0 
u = np.linspace(-3.14, 3.14, 50)
X = 2*np.cos(u)
Y = 2*np.sin(u)
Z = u + 1
ax.plot(X, Y, Z, color='g')"""

###############################
# Exo 8, section 5-2
def fct(x):
	return 6 - x**2

fig = plt.figure()

NbOfImages = 201
i = 0
while (i <= NbOfImages-1):
	ax = fig.gca(projection = '3d')

	ax.set_xlim3d(-7, 7)
	ax.set_ylim3d(-7, 7)
	ax.set_zlim3d(-7, 7)

	t = (i*6.28)/(NbOfImages-1)
	paramX = np.linspace(-2,2, 100)
	paramTheta = np.linspace(0, t, 100)
	x, theta = np.meshgrid(paramX, paramTheta)
	X = x 

	# Surface of revolution
	Y = fct(x)*np.cos(theta)
	Z = fct(x)*np.sin(theta)
	ax.plot_surface(X, Y, Z, color='b', alpha=0.7, rstride=2, cstride = 2)
	
	# Cylinder in the middle (become solid)
	Y = 2*np.cos(theta)
	Z = 2*np.sin(theta)
	ax.plot_surface(X, Y, Z, color='b', alpha=0.7, rstride=2, cstride=12)
	
	# The x-axis
	X = np.linspace(-6, 6, 100)
	Y = 0*X 
	Z = 0*Y 
	ax.plot(X, Y, Z, color='r', alpha=0.7)
	
	plt.savefig('Revolution' + str(i) + '.png') #f"{i:03}" + '.png')
	if (i < NbOfImages - 1):
		plt.clf()
	i+=1

plt.show()

fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.set_xlim3d(-2, 2)
ax.set_ylim3d(-7, 7)
ax.set_zlim3d(-7, 7)

paramX = np.linspace(-2,2, 100)
paramTheta = np.linspace(0, 6.28, 100)
x, theta = np.meshgrid(paramX, paramTheta)
X = x 
Y = fct(x)*np.cos(theta)
Z = fct(x)*np.sin(theta)
ax.plot_surface(X, Y, Z, color='r', alpha=0.7, rstride=2, cstride = 12)

Y = 2*np.cos(theta)
Z = 2*np.sin(theta)
ax.plot_surface(X, Y, Z, color='r', alpha=0.7, rstride=2, cstride=12)

plt.show()