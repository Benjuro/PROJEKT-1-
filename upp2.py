import numpy as np
import matplotlib.pyplot as plt

f0 = 3 * np.pi
f = 2 * np.pi
b = 0.1
y = np.array([0,0])
T = 9.9
N = 800
k = T/N
tn = 0 
time = []
position = []
def F(t, u):
    return np.array([u[1], - f0 * f0 * u[0] + b * f0 * f0 * np.cos(f * t)])

def g(t):
    if f0 == f:
        return (b * f0 * t )/2 * np.sin(f0 * t)
    else:
        return ((b * f0 * f0)/(f0 * f0 - f * f)) * (np.cos(f * t) - np.cos(f0 * t))


for i in range(N):
    w1 = F(tn, y)
    w2 = F(tn + k/2, y + k/2 * w1)
    w3 = F(tn + k/2, y + k/2 * w2)
    w4 = F(tn + k, y + k*w3)
    y = y + k/6 * (w1 + 2*w2 + 2*w3 + w4)
    tn += k
    time.append(tn)
    position.append(y[0])

plt.scatter(time, position)
plt.ylabel("\u03B8 [rad]")
plt.xlabel("t [s]")
plt.grid()
plt.show()

solution = g(np.array(time))
print(np.abs(solution[len(solution) - 1] - position[len(position) - 1]))








