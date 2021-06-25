import numpy as np

print("\nReading from a text file:")
file_data = np.genfromtxt("file", delimiter=" ", dtype="int32")
print(file_data)

print("\nBoolean masking:")
print(file_data > 4)
print(file_data[file_data <= 3])

print("\nIndexing with a list:")
a = np.array([1, 2, 3, 4, 5], dtype="int32")
print(a)
print(a[[0, 3, 4]])


