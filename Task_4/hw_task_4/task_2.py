import numpy as np


m = np.zeros((8, 8), dtype=int)
m[1::2, ::2] = 1
m[::2, 1::2] = 1
print(m)