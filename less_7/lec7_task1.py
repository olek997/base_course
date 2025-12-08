import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-2, 3)
ax.set_ylim(-2, 3)
ax.axis('equal')
anim_obj, = plt.plot([], [], 'o')

Vx = 2
Vy = 4
g = 10
x = []
y = []

def update(t):
    x.append(Vx * t)
    y.append(Vy*t - (g*(t)**2)/2)
    anim_obj.set_data(x, y)
    return anim_obj,

	
anim = FuncAnimation(fig, 
                    update, 
                    frames=np.arange(0, 2*np.pi, 0.01),
                    interval=100 ,
                    )            
 
anim.save('animation1.gif')