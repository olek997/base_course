import numpy as np 
import constant as cst
import math as m
h = 100
alpha = 45
beta = 35
v = np.sqrt((cst.g * h * np.tan(beta)**2)/2*np.cos(alpha)**2*(1 - np.tan(beta) * np.tan(alpha)))
print(v)