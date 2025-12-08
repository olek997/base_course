import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-2, 3)
ax.set_ylim(-2, 3)
ax.axis('equal')
anim_obj, = plt.plot([], [])

x = []
y = []

def gen_data_for_circle(R):
    alpha = np.linspace(0, 2 * np.pi, 100)
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    return x, y

def update(t): 
   x, y = gen_data_for_circle(t)
   anim_obj.set_data(x, y)
   return anim_obj

	
anim = FuncAnimation(fig, 
                    update, 
                    frames=np.arange(0, 2*np.pi, 0.01),
                    interval=100,
                    )            
 
anim.save('animation2.gif')