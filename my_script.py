import time
import numpy as np

print("Starting computation...")

# Simulate computation load
size = 500
A = np.random.rand(size, size)
B = np.random.rand(size, size)

result = np.dot(A, B)

# Simulate delay
time.sleep(3)

print("Computation complete!")
