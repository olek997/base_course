import matplotlib.pyplot as plt
import numpy as np


k = 2
x = np.arange(-5, 5, 0.01)
y = k/x

plt.plot(x, y, label='my parabola')
plt.savefig('fig2.png')