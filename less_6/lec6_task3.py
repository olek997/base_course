import matplotlib.pyplot as plt
import numpy as np
A = 3
B = 1
 
x = np.arange(-2, 2, 0.01)
y = np.arange(-2, 2, 0.01)
 
X, Y = np.meshgrid(x, y)

plt.contour(X, Y, (X**2)/A + (Y**2)/B, levels=[1])
plt.axis("equal")   
plt.savefig('fig3.png')
