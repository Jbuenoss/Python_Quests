import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection="3d")

x = np.arange(1, 100, 0.1)
y = np.sin(x)
z = np.cos(x)

ax.plot(x, y, z)
ax.set_xlabel("Values of x")
ax.set_ylabel("Sin of x")
ax.set_zlabel("Cos of x")
ax.set_title("3D Plot")

plt.show()