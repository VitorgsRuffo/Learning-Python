import numpy as np

print("\nReshaping arrays:")
before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]], dtype="int32")
print("\nBefore:")
print(before)

after = before.reshape((4, 2))
print("\nAfter:")
print(after)

after = before.reshape((8, 1))
print("\nAfter:")
print(after)

after = before.reshape((2, 2, 2))
print("\nAfter:")
print(after)

print("\nVertically Stacking arrays:")
a = np.array([1, 2, 3])
b = np.array([7, 8, 9])
print(np.vstack([a, b, a, b, b]))

print("\nHorizontally Stacking arrays:")
a = np.ones((2, 4))
b = np.zeros((2, 2))
print(np.hstack([b, a, b]))
