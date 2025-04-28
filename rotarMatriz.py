import numpy as np
import matplotlib.pyplot as plt

point = np.array([3, 4])
thetar = 20 *np.pi / 180  # Convert degrees to radians
R = np.array([[np.cos(thetar), -np.sin(thetar)],
              [np.sin(thetar), np.cos(thetar)]])

point_rotated = np.dot(R, point)  # Rotate the point

print("Original point:", point)
print("Rotated point:", point_rotated)
