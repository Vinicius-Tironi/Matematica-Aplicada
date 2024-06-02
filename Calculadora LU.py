# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import math
pi = math.pi
pi2 = pi**2

# Decomposição LU para solução do sistema AX = Y:
# A = LU => (LU)X = Y => L(UX) = Y =>   LZ = Y    <= Z = UX;
# Resolve-se LZ = Y por substituição avançada e então UX = Z por susbtituição atrasada.

def calculadora_LU(matrix: list) -> tuple:  # Decomposição LU

    n_matrix = len(matrix)

    U = matrix
    L = [[(1 if i == j else 0) for j in range(n_matrix)] for i in range(n_matrix)]
   
    pivo_atual = 0
    for i in range(n_matrix):
        for j in range(i+1, n_matrix):
            operador = -1 * (matrix[j][pivo_atual]/matrix[i][pivo_atual])
            L[j][pivo_atual] = -operador

            for x in range(pivo_atual, n_matrix):
                U[j][x] += operador * U[i][x]
        pivo_atual += 1                

    return L, U


def calculo_z(L: list, y: list) -> list: # Substituição avançada

    n_L = len(L)

    pivo_atual = 0
    for i in range(n_L):
        for j in range(i+1, n_L):
            operador = -1 * (L[j][pivo_atual]/L[i][pivo_atual])
            y[j] += operador * y[i]            
        pivo_atual += 1      

    return y


def calculo_x(U: list, z: list) -> list: # Substituição atrasada
    n_U = len(U)
    pivo_atual = n_U-1
    for i in range(n_U-1, -1, -1):

        for j in range(i-1, -1, -1):
            operador = -1 * (U[j][pivo_atual]/U[i][pivo_atual])
            z[j] += operador * z[i]
        pivo_atual -= 1

    pivo_atual = 0
    for i in range(n_U):
        z[i] /= U[i][pivo_atual]
        pivo_atual += 1

    return z


# Sendo A uma matriz quadrada
n_matrix, quantidade_y = input("Dimensão (nxn) da matriz e Quantidade de vetores Y\n").split(' ')
n_matrix, quantidade_y = int(n_matrix), int(quantidade_y)
print("Dimensão da matriz =", n_matrix)
print("Quantidade de vetores Y =", quantidade_y)


# Definir matriz A
A = []
for _ in range(n_matrix):
    A.append([float(x) for x in input("Linha da matriz\n").split(' ')])
print("A = " , A)

# Calculo de L,U para decompor A = LU
L, U = calculadora_LU(A)    


# Definir quantidade de vetores
for _ in range(quantidade_y):

    y = [float(x) for x in input("Vetor Y\n").split(' ')]

    z = calculo_z(L, y)
    print("Z = " , *z)
    
    x = calculo_x(U, z)
    print("X = ", *x)


valores_x = []     # Valores nas coordenadas x
h = 1/6            # Distância entre os pontos
X = h
m = (1/h)-1        # Quantidade de pontos
M = int(m)
#print(M)

for i in range(0,M):
    valores_x.append(X)
    X = X + h
    

# Gráfico

plt.plot(valores_x , x, label = 'Solução Numérica', linestyle='--')
plt.scatter(valores_x, x)
#plt.hlines(y=0, xmin=0, xmax=1 , colors='black', linestyles='--')

#plt.yticks(np.arange(-1.6, 1.6, 0.2))

plt.legend(loc="upper right", prop={'size': 8})
plt.grid()
plt.show()


