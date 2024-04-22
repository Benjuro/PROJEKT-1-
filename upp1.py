
import numpy as np
import matplotlib.pyplot as plt

def f(f0, f, b, t):
    if f0 == f:
        return (b * f0 * t )/2 * np.sin(f0 * t)
    else:
        return ((b * f0 * f0)/(f0 * f0 - f * f)) * (np.cos(f * t) - np.cos(f0 * t))

T = np.linspace(0,10,1000)

plt.plot(T, f(3 * np.pi, 2 * np.pi, 0.1, T), label = "\u03C9\u2080 \u2260 \u03C9 ")
plt.ylabel("\u03B8 [rad]")
plt.xlabel("t [s]")
plt.legend()
plt.show()
plt.plot(T, f(3 * np.pi, 3 * np.pi, 0.1, T),  label = "\u03C9\u2080 = \u03C9")
plt.ylabel("\u03B8 [rad]")
plt.xlabel("t [s]")
plt.legend()
plt.show()
