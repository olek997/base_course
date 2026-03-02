import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import constant as cst
'''M = 8*54*10**36
r = 10000
R = 6732.005 * 10**6'''
M_sun = 1.9885*10**30
R_sun = 695710000
alpha = (4 * cst.G * M_sun) / (cst.c**2 * R_sun)
print(alpha)
x_sun = np.arange(-2, 2, 0.01)
y_sun = np.arange(-2, 2, 0.01)
 
X_sun, Y_sun = np.meshgrid(x_sun, y_sun)


t_array = np.arange(-1, 1, 0.01)
x_array = t_array
y_array = t_array
plt.plot((x_array-0.5)*np.cos(alpha), (y_array + 1.5) *np.sin(alpha))
plt.contour(X_sun, Y_sun, (X_sun**2) + (Y_sun**2), levels=[1])
plt.axis("equal")   
plt.savefig('azalupka.png')