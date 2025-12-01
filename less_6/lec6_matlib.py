import matplotlib.pyplot as plt
import numpy as np
 
x = np.arange(-2, 2, 0.1)
y = np.arange(-2, 2, 0.1)
 
X, Y = np.meshgrid(x, y)
v =2 
m = 1
c = 2

plt.contour(X, Y, X**2+Y**2, levels=[1])
plt.axis('equal')   
plt.savefig('fig_4.png')
