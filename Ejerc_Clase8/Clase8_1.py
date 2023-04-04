import random as rand
import numpy as np

def matrices(filas,columnas):
    matriz=[]
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            num = rand.randint(1,10)
            matriz[i].append(num)
    return matriz
matriz=matrices(5,10)
print(matriz)
mayor = matriz[0][0]
menor = matriz[0][0]

for i in matriz:
    for j in i:
        if j > mayor:
            mayor = j
        if j < menor:
            menor = j
for i in range(5):
    for j in range(10):
        if matriz[i][j] == menor:
            posc_menor = str(i) + str(j)
        if matriz[i][j] == mayor:
            posc_mayor = str(i) + str(j)
print(f'El menor es {menor} y esta en la posicion {posc_menor} el mayor es {mayor} y esta en la poscion {posc_mayor}')

def ordenar(filas,columnas,matriz):
    lista=[]
    for i in range(filas):
        for j in range(columnas):
           lista.append(matriz[i][j])
    lista.sort()
    matriz_ord = np.array(lista).reshape(filas,columnas)
    return matriz_ord
ordenar(5,10,matriz)