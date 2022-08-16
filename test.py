import numpy as np
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,2,3,4,5]
z=np.array([[1],[2],[3],[4],[5]])
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z,cmap='viridis')

plt.show()