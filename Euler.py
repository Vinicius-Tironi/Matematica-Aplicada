# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt


def X(T):
    f = 3 - 2*np.exp(-3*T)
    return f

def Y(T):
    g = 3 - np.exp(-3*T)
    return g

def Z(T):
    h = 3 + 3*np.exp(-3*T)
    return h

T = np.linspace(0, 2)
plt.plot(T, X(T), color='blue' , label = 'Solução Analítica para x(t)')
plt.plot(T, Y(T), color='green', label = 'Solução Analítica para y(t)')
plt.plot(T, Z(T), color='red', label = 'Solução Analítica para z(t)')
plt.legend(loc="upper right" , prop={'size': 15})
plt.xlabel('t')
plt.grid()


# Euler

x0,y0,z0 = input("Insira as condições iniciais (x0, y0 e z0)\n").split(' ')
x0,y0,z0 = float(x0), float(y0), float(z0)

h = input("Defina o comprimento dos passos (h)\n")
h = float(h)
n_passos = input("Defina o número de passos (n)\n")
n_passos = int(n_passos)

v_t = np.zeros(n_passos + 1)
v_x = np.zeros(n_passos + 1)
v_y = np.zeros(n_passos + 1)
v_z = np.zeros(n_passos + 1)

v_t[0] = 0
v_x[0] = x0
v_y[0] = y0
v_z[0] = z0

for i in range(n_passos):
    t = v_t[i]
    x = v_x[i]
    y = v_y[i]
    z = v_z[i]
    
    f_x = -2*x + y + z
    f_y = x - 2*y + z
    f_z = x + y - 2*z

    x_n = x + h * f_x
    y_n = y + h * f_y
    z_n = z + h * f_z
    
    v_t[i+1] = t + h
    v_x[i+1] = x_n
    v_y[i+1] = y_n
    v_z[i+1] = z_n


plt.plot(v_t, v_x, label='Método de Euler para x(t)', color = 'fuchsia' , linestyle = '--')
plt.plot(v_t, v_y, label='Método de Euler para y(t)', color = 'darkorange' , linestyle = '--')
plt.plot(v_t, v_z, label='Método de Euler para z(t)', color = 'darkmagenta' , linestyle = '--')
plt.legend(loc="upper right" , prop={'size': 15})
plt.xlabel('t')
plt.grid()
plt.show()