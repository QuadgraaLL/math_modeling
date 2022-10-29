from lab_3_task_1 import acceleration_of_gravity as g
from lab_3_task_1 import Boltzmann_constant as k
from lab_3_task_1 import euler_number as e
from lab_3_task_1 import constant_plank as h


import numpy as np

x1 = g*h * np.tan(30) ** 2
x2 = 2 * np.cos(np.pi / 3) * (1 - np.tan(30) * np.tan(np.pi / 3))
v = np.sqrt(x1 / x2)

print(v)

T = 200
E = 300

x1 = 2 / np.sqrt(np.pi) 
x2 = h / (k*T) ** 1.5 
x3 = e ** (-E / k*T) * E ** (T / 2)
N = x1 * x2 * x3
print(N)