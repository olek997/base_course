import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import solve_ivp
M = 1.0         
R_star = 3.0      
b_values = [7, 10, 13, 16]

def ugol(phi, y):
    return [y[1], 3 * M * y[0]**2 - y[0]]

paths = []
for b in b_values:

    x0, y0 = -40, b
    r0 = (x0**2 + y0**2)**0.5
    phi0 = np.pi - np.arcsin(b/r0)
    
    sol = solve_ivp(ugol, [phi0, 0], [1/r0, np.cos(phi0)/b], 
                    max_step=0.05, rtol=1e-6)
    
    r = 1.0 / sol.y[0]
    paths.append({
        'x': r * np.cos(sol.t),
        'y': r * np.sin(sol.t)
    })
#background
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_aspect('equal')
ax.set_xlim(-30, 30)
ax.set_ylim(-20, 20)
ax.axis('off') 
#star
star_glow = plt.Circle((0, 0), R_star*1.3, color='orange', alpha=0.15)
star_body = plt.Circle((0, 0), R_star, color='yellow', ec='orange', lw=2)
ax.add_patch(star_glow)
ax.add_patch(star_body)
#rays
rays = [ax.plot([], [], color='white', lw=1.5, alpha=0.8)[0] for _ in paths]

def animate(frame):
    for i, path in enumerate(paths):
        end = int(frame * (len(path['x']) / 100))
        rays[i].set_data(path['x'][:end], path['y'][:end])
    return rays

ani = animation.FuncAnimation(fig, animate, frames=100, interval=30, blit=True)
ani.save('light_bending.gif', writer='pillow')
plt.show()