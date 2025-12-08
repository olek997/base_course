import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.axis('equal')
anim_obj, = plt.plot([], [])

def gen_heart(A):
    t = np.linspace(0, 2*np.pi, 100)
    x = (16*(np.sin(t)**3))* A
    y = (13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)) * A
    return x, y

def update(t):
   x, y = gen_heart(t)
   anim_obj.set_data(
    x, 
    y
    )
   return anim_obj

	
anim = FuncAnimation(fig, 
                    update, 
                    frames=np.arange(0, 2*np.pi, 0.01),
                    interval=100,
                    )            
 
anim.save('animation4.gif')