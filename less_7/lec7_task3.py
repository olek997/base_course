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
a = 2
w = 1
k = 1

def gen_struna(t):
    x = np.linspace(-1, 2 * np.pi, 100)
    y = a*np.sin(k*x)*np.cos(w*t)
    return x, y

def update(t):
   x, y = gen_struna(t)
   anim_obj.set_data(
    x, 
    y
    )
   return anim_obj

	
anim = FuncAnimation(fig, 
                    update, 
                    frames=np.arange(0, 2*np.pi, 0.1),
                    interval=100,
                    )            
 
anim.save('animation3.gif')