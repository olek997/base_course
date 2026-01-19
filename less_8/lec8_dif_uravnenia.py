import sympy as sym
import scipy.integrate as sci
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 4, 0.01)
a0 = 10
gamma = 1
def skorost(x, t):
    return gamma * x**2 

kolvo = sci.odeint(skorost, a0, t)

plt.plot(t, kolvo)
#plt.axis('equal')
plt.savefig('fig.png')