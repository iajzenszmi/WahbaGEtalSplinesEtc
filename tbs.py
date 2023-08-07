import numpy as np
from scipy.interpolate import Rbf
import matplotlib.pyplot as plt

# Sample data
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 0, 1, 0])
z = np.array([1, 4, 1, 4, 1])

# Create the interpolator
rbf = Rbf(x, y, z, function='thin_plate')

# Create a grid to evaluate the interpolator
xi, yi = np.meshgrid(np.linspace(0, 4, 100), np.linspace(0, 1, 100))
zi = rbf(xi, yi)

# Plot the original points
plt.scatter(x, y, c=z, s=100, marker='o')

# Plot the interpolated surface
plt.imshow(zi, extent=[0, 4, 0, 1], origin='lower', cmap='viridis', alpha=0.5)
plt.colorbar(label='Z Value')
plt.title('Thin-Plate Spline Interpolation')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
print (rbf)
