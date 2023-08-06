import numpy as np
from scipy.interpolate import Rbf
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Assume we have some data on a sphere
longitude = np.random.uniform(-np.pi, np.pi, size=(100,))
latitude = np.random.uniform(-np.pi/2, np.pi/2, size=(100,))
data = np.random.uniform(-1, 1, size=(100,))

# Convert to Cartesian coordinates
x = np.cos(latitude) * np.cos(longitude)
y = np.cos(latitude) * np.sin(longitude)
z = np.sin(latitude)

# Fit RBF to the data
rbf = Rbf(x, y, z, data, function='multiquadric')

# Define grid for plotting
longitude_grid, latitude_grid = np.meshgrid(np.linspace(-np.pi, np.pi, 100), np.linspace(-np.pi/2, np.pi/2, 100))
x_grid = np.cos(latitude_grid) * np.cos(longitude_grid)
y_grid = np.cos(latitude_grid) * np.sin(longitude_grid)
z_grid = np.sin(latitude_grid)

# Evaluate RBF at grid points
data_grid = rbf(x_grid, y_grid, z_grid)

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c=data)
ax.plot_surface(x_grid, y_grid, z_grid, rstride=1, cstride=1, facecolors=plt.cm.viridis(data_grid), alpha=0.5, linewidth=0)
plt.show()

