import numpy as np
from scipy.interpolate import Rbf
import matplotlib.pyplot as plt

# Define original data
x = np.random.rand(100)*4.0-2.0
y = np.random.rand(100)*4.0-2.0
z = x*np.exp(-x**2 - y**2)

# Define grid upon which to interpolate
ti = np.linspace(-2.0, 2.0, 100)
XI, YI = np.meshgrid(ti, ti)

# Use RBF
rbf = Rbf(x, y, z, function='thin_plate')
ZI = rbf(XI, YI)

# Plot the result
plt.pcolor(XI, YI, ZI, cmap=plt.cm.jet)
plt.scatter(x, y, 100, z, cmap=plt.cm.jet)
plt.title('RBF interpolation - multiquadrics')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.colorbar()
plt.show()

