import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-100,100,1000)
y = np.linspace(-100,100,1000)
A = np.meshgrid(x,y)

plt.scatter(A[0], A[1])
plt.show()
