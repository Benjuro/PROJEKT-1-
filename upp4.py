import numpy as np
import scipy.integrate as ode
import matplotlib.pyplot as plt


f = 2 * np.pi
f0 = 3/2 * f
beta = 1/4 * f0
b = 1.06
y = np.array([0,0])
T = 40
N = 800
k = T/N
tn = 0 
time = []
t = np.linspace(0,T, N)
position = []


def F(t, u):
    return np.array([u[1], - f0 * f0 * np.sin(u[0]) - 2 * beta * u[1] + b * f0 * f0 * np.cos(f * t)])


SOL = ode.solve_ivp(F,(0,T) , y, method='RK45', t_eval = t)
plt.plot(t, SOL.y[0], label = f"\u03B3 = {b}")
plt.ylabel("\u03B8 [rad]")
plt.xlabel("t [s]")
plt.legend()
plt.grid()
plt.show()


b = 1.07
SOL = ode.solve_ivp(F,(0,T) , y, method='RK45', t_eval = t)
plt.plot(t, SOL.y[0], label = f"\u03B3 = {b}")
plt.ylabel("\u03B8 [rad]")
plt.xlabel("t [s]")
plt.legend()
plt.grid()
plt.show()

b = 1.16
SOL = ode.solve_ivp(F,(0,T) , y, method='RK45', t_eval = t)
plt.plot(t, SOL.y[0], label = f"\u03B3 = {b}")
plt.ylabel("\u03B8 [rad]")
plt.xlabel("t [s]")
plt.legend()
plt.grid()
plt.show()




