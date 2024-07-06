# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt

# Runge-Kutta de Quarta Ordem

def X(t, x, y, z):
    X = -2*x + y + z 
    return X

def Y(t, x, y, z):
    Y = x - 2*y + z
    return Y

def Z(t, x, y, z):
    Z = x + y - 2*z
    return Z

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


for i in range(n_passos):  # Runge-Kutta de Quarta Ordem
    t = v_t[i]
    x = v_x[i]
    y = v_y[i]
    z = v_z[i]    
    
    k1 = h * X(t, x, y, z)
    l1 = h * Y(t, x, y, z)
    j1 = h * Z(t, x, y, z)
    
    k2 = h * X(t + h/2, x + k1/2, y + l1/2, z + j1/2)
    l2 = h * Y(t + h/2, x + k1/2, y + l1/2, z + j1/2)
    j2 = h * Z(t + h/2, x + k1/2, y + l1/2, z + j1/2)
    
    k3 = h * X(t + h/2, x + k2/2, y + l2/2, z + j2/2)
    l3 = h * Y(t + h/2, x + k2/2, y + l2/2, z + j2/2)
    j3 = h * Z(t + h/2, x + k2/2, y + l2/2, z + j2/2)
    
    k4 = h * X(t + h, x + k3, y + l3, z + j3)
    l4 = h * Y(t + h, x + k3, y + l3, z + j3)
    j4 = h * Z(t + h, x + k3, y + l3, z + j3)
    
    v_x[i+1] = x + (k1 + 2*k2 + 2*k3 + k4) / 6
    v_y[i+1] = y + (l1 + 2*l2 + 2*l3 + l4) / 6
    v_z[i+1] = z + (j1 + 2*j2 + 2*j3 + j4) / 6
    v_t[i+1] = t + h
    
    

plt.plot(v_t, v_x, label='Runge Kutta para x(t)', color = 'magenta' , linestyle = '--')
plt.plot(v_t, v_y, label='Runge Kutta para y(t)', color = 'yellow', linestyle = '--')
plt.plot(v_t, v_z, label='Runge Kutta para z(t)', color = 'mediumaquamarine', linestyle = '--')
plt.legend(loc="upper right" , prop={'size': 15})
plt.xlabel('t')
plt.legend()
plt.grid()
plt.show()
