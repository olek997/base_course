import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Circle

M = 3.0
G = 1.0
c = 1.0

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
glow = Circle((0, 0), 2.5, color='yellow', alpha=0.2)
ax.add_patch(glow)

def calculate_ray(b):
    x = np.linspace(x_min, x_max, 300)
    theta = 4 * G * M / (c**2 * b)
    y = np.zeros_like(x)
    
    for i, xi in enumerate(x):
        if xi < 0:
            y[i] = b
        else:
            distance_effect = np.exp(-xi/4)
            y[i] = b - theta * xi * distance_effect
    
    return x, y

rays = []
ray_data = []

for i, (b, color) in enumerate(zip(b_values, colors)):
    x, y = calculate_ray(b)
    ray_data.append((x, y))
    
    ray, = ax.plot([], [], color=color, linewidth=2, label=f'b = {b}')
    rays.append(ray)

ax.legend(loc='upper right')

info_text = ax.text(0.02, 0.98, '', transform=ax.transAxes,
                    verticalalignment='top',
                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

def init():
    for ray in rays:
        ray.set_data([], [])
    info_text.set_text('')
    return rays + [info_text]

def animate(frame):
    
    progress = frame / 50

    max_x = x_min + (x_max - x_min) * progress
    
    for i, (ray, (x, y)) in enumerate(zip(rays, ray_data)):
        mask = x <= max_x
        ray.set_data(x[mask], y[mask])
    info = f"Кадр: {frame}/50\n"
    info += f"Прогресс: {progress*100:.0f}%\n\n"
    
    for i, b in enumerate(b_values):
        theta = 4 * G * M / (c**2 * b)
        info += f"b={b:.1f}: {np.degrees(theta):.1f}°\n"
    
    info_text.set_text(info)
    
    return rays + [info_text]



anim = FuncAnimation(fig, animate, init_func=init, 
                     frames=51, interval=100, blit=True)

writer = PillowWriter(fps=10)
anim.save('light_deflection.gif', writer=writer)
plt.show()