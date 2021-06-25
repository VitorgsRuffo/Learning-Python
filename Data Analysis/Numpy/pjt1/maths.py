import numpy as np

# (https://docs.scipy.org/doc/numpy/reference/routines.math.html)

a = np.array([1, 2, 3], dtype="int32")
b = np.array([4, 5, 6], dtype="int32")

print("\nPerforming an operation on each element of an array:")
print(a)
print(a+1)
print(a*2)

print("\nOperating on two arrays:");
print(a + b)
print(a * b)

print("\nCalculating the sin of each value in an array:")
sin_a = np.sin(a)
print(sin_a)


# Linear algebra stuff:
# (https://docs.scipy.org/doc/numpy/reference/routines.linalg.html)

print("\nMultiplying matrices (linear algebra):")
a = np.full((3, 2), 2)
b = np.full((2, 4), 4)
print(np.matmul(a, b))


