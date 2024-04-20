import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as ode

f0 = 3 * np.pi
f = 2 * np.pi
b = 0.1
y = np.array([0,0])
T = 9.9
N = 200
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
    y = k/6 * (w1 + 2*w2 + 2*w3 + w4)
    tn += k
    time.append(tn)
    position.append(y[0])

SOL = ode.solve_ivp(F, (0,T), y, method='RK45', rtol=1e-10, atol=1e-10)
plt.scatter(SOL.t, SOL.y[0])
plt.scatter(time, position)
plt.show()



print("heheh")






