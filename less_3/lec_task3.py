import numpy as np
import constant as cst
v_0x = 4
v_0y = 0
x0 = 0
y0 = 123
n = 6
t = 0
b = np.zeros((n, 3))
b[::, 0] = np.linspace(0, 5, n)
b[::, 1] = x0 + v_0x * b[::, 0]
b[::, 2] = y0 + v_0y * b[::, 0] - (cst.g * (b[::, 0]**2)/2)
print(b)
    