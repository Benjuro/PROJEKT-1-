
import numpy as np
import matplotlib.pyplot as plt



def f(f0, f, b, t):
    if f0 == f:
        return (b * f0 * t )/2 * np.sin(f0 * t)
    else:
        return ((b * (f0 ** 2))/(f0**2 - f**2)) * (np.cos(f * t) - np.cos(f0 * t))

T = np.linspace(0,10,1000)

plt.title("\u03C9\u2080 = 260 ")
plt.scatter(T, f(3 * np.pi, 2 * np.pi, 0.1, T))
plt.show()
plt.scatter(T, f(3 * np.pi, 3 * np.pi, 0.1, T))
plt.show()
