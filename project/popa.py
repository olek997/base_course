import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
from scipy.integrate import odeint
import warnings
warnings.filterwarnings('ignore')
G = 1.0
M = 1.0
c = 1.0
Rs = 2*G*M/c**2
b_values = [3.5, 4.0, 5.0, 6.0, 8.0]
colors = ['red', 'blue', 'green', 'purple', 'orange']

def photon_path(b, phi_max = np.pi):
    u0 = 1e - 6
    du_dphi0 = 0

def orbit_equation(y, phi):
    u, du = y
    d2u = -u + 3 *G * M * u**2/ c**2
    return [du, d2u]
    phi = np.linspace(-phi_max, phi_max, 1000)
    solution = odeint(orbit_equation, [u0, du_dphi0], phi)
    u = solution[:, 0]

    r = 1/u
    x = r * np.cos(phi)
    y = r * np.sin(phi) + b 
 
    scale = 5.0
    x = x/scaley = (y - b) /scale

    return x, y