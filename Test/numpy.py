import numpy as np 
a = np.array([1,2,3]) 
print(a)

# more than one dimensions
a = np.array([[1, 2], [3, 4]]) 
print(a)

# minimum dimensions
a = np.array([1, 2, 3,4,5], ndmin = 2) 
print(a)

# dtype parameter 
a = np.array([1, 2, 3], dtype = complex) 
print(a)

# using array-scalar type
dt = np.dtype(np.int32) 
print(dt)

dt = np.dtype('i4')
print(dt) 

dt = np.dtype([('age',np.int8)]) 
print(dt)


