import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('equal')
animation_object = plt.plot([], [])

x = []
y = []

def update(frame):
    x.append(np.cos(frame))
    y.append(np.sin(frame))
    animation_object.set_data([np.cos(frame)], [np.sin(frame)])
    return animation_object

animation = FuncAnimation(fig,
                          update,
                          frames = np.arange(0, 2 * np.pi, 0.01),
                          interval = 100
                          )
animation.save('animatioin.gif')