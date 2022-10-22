import numpy as np

a = [4, 16, 10, 5, 7, 1, 8]
slice = a[2:5:1]
print(slice)

slice = a[3:0:-1]
print(slice)

slice = a[::-1]
print(slice)

b = np.array([a, np.array(a) * 3])
print(b)
slice = b[::, 1]
print(slice)

slice - b[1,2::3]
print(slice)