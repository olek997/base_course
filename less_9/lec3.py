import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
'''fig, ax = plt.subplots()

anim_obj, = plt.plot([], [])
def update(t):
    A = t
    x_array = np.arange(-4*np.pi, 4*np.pi, 0.01)
    y_array = A * np.sin(x_array)
    anim_obj.set_data(x_array, y_array)
    return anim_obj

A_array = np.arange(0.5, 3.0, 0.25)
ani = FuncAnimation(fig,
                    update,
                    frames = A_array)
ax.set_xlim(-4*np.pi, 4*np.pi)
ax.set_ylim(-4*np.pi, 4*np.pi)
ani.save('animation_sin.gif')'''
fig, ax = plt.subplots()

anim_obj, = plt.plot([], [])
def update_radius(R):
    a = np.linspace(0, 4 * np.pi, 100)
    x = 1.5*R * np.cos(a)
    y = R * np.sin(a)
    return x, y
def update(t):
    x, y = update_radius(t)
    anim_obj.set_data(x+1.5*t, y+1.5*t)
    return anim_obj
x = []
y = []

anim = FuncAnimation(fig, 
                    update, 
                    frames=np.arange(0, 4*np.pi, 0.1),
                    interval=100,
                    )
ax.set_xlim(-4*np.pi, 4*np.pi)
ax.set_ylim(-4*np.pi, 4*np.pi)  
anim.save('animation_elipse.gif')


    
