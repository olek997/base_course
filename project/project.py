import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Circle

M = 3.0
m = 0.01
G = 1.0
c = 1.0
v_x = 100
v_y = 0

b_values = [2.5, 3.5, 4.5, 6.0]  
colors = ['red', 'orange', 'green', 'blue']
x_min, x_max = -12, 12
y_min, y_max = -4, 8
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)

ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_xlabel('X координата')
ax.set_ylabel('Y координата')
ax.set_title('Искривление света вблизи массивной звезды')

star = Circle((0, 0), 1.8, color='orange', alpha=0.8, label='Звезда')
ax.add_patch(star)
def update(t):
    t = np.linspace(0, 5, 100)
    x = v_x*t
    y = v_y * t