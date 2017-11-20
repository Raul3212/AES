import random as rnd 
import math as mt

def list2matrix(lista, n):
	matrix = []
	for i in range(0, len(lista), n):
		matrix.append(lista[i:i+n])
	return matrix

def rotateList(lista, n):
	return lista[n:] + lista[0:n]

def hexMatrix(matrix):
	return [[hex(x) for x in line] for line in matrix]

def xorList(lista1, lista2):
    listaXor = []
    for i in range(0, len(lista1)):
        listaXor.append(lista1[i] ^ lista2[i])
    return listaXor

def xorKey(estado, subChave):
    newEstado = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            newEstado[i][j] = estado[i][j] ^ subChave[i][j]
    return newEstado