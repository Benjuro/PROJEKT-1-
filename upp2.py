import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-100,100,1000)
y = np.linspace(-100,100,1000)
A = np.meshgrid(x,y)
#Benjamin fucking hora sluta förstör koden RAAAAAAAAAAAAAAAAAAAAAAAAAAAH
#tetseegeg
plt.scatter(A[0], A[1])
plt.grid()
plt.show()

