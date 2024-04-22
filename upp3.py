import numpy as np
import matplotlib.pyplot as plt

f0 = 3 * np.pi
f = f0
b = 0.1
y = np.array([0,0])
T = 40
N = 800
k = T/N
tn = 0 
time = []
position = []
def F(t, u):
    return np.array([u[1], - f0 * f0 * u[0] + b * f0 * f0 * np.cos(f * t)])

for i in range(N):
    w1 = F(tn, y)
    w2 = F(tn + k/2, y + k/2 * w1)
    w3 = F(tn + k/2, y + k/2 * w2)
    w4 = F(tn + k, y + k*w3)
    y = y + k/6 * (w1 + 2*w2 + 2*w3 + w4)
    tn += k
    time.append(tn)
    position.append(y[0])



plt.plot(time, position, label = "\u03C9\u2080 = \u03C9")
plt.ylabel("\u03B8 [rad]")
plt.xlabel("t [s]")
plt.grid()
plt.legend()
plt.show()

f = 2 * np.pi
time = []
position = []
y = np.array([0,0])
tn = 0 


for i in range(N):
    w1 = F(tn, y)
    w2 = F(tn + k/2, y + k/2 * w1)

    w3 = F(tn + k/2, y + k/2 * w2)
    w4 = F(tn + k, y + k*w3)
    y = y + k/6 * (w1 + 2*w2 + 2*w3 + w4)
    tn += k
    time.append(tn)
    position.append(y[0])

plt.plot(time, position,  label = "\u03C9\u2080 ≠ \u03C9")
plt.ylabel("\u03B8 [rad]")
plt.xlabel("t [s]")
plt.grid()
plt.legend()
plt.show()

time = []
position = []
y = np.array([0,0])
tn = 0 
N = 10000
k = T/N

for i in range(N):
    y = y + k * F(tn, y)
    tn += k
    time.append(tn)
    position.append(y[0]) 

plt.plot(time, position,  label =f"k = {k}")

plt.ylabel("\u03B8 [rad]")
plt.xlabel("t [s]")
plt.grid()
plt.legend()
plt.show()

#