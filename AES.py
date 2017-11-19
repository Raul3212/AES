import numpy as np
from util import *
import math as mt
import copy
import random as rnd 

# Regra da multiplicação (Eq. 4.14)
xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

def initEstado(n):
	estado = []
	for i in range(n):
		estado.append(rnd.randint(0, n-1))
	return list2matrix(estado, int(mt.sqrt(16)))

def initSBox(n):
	sBox = []
	for i in range(n):
		sBox.append(i)
	return sBox


def subBytes(estado, sBox):
	print(" [>>>] SUB BYTES")
	newEstado = copy.copy(estado)
	for i in range(4):
		for j in range(4):
			newEstado[i][j] = sBox[estado[i][j]]
	print(" [?] ESTADO:\n{}".format(np.matrix(newEstado)))
	return newEstado

def shiftRows(sBox):
	print(" [>>>] SHIFT ROWS")
	newEstado = []
	for i in range(len(sBox)):
		newEstado.append(rotateList(sBox[i], i))
	print(" [?] ESTADO:\n{}".format(np.matrix(newEstado)))
	return newEstado


def mixColumns(estado):
	print(" [>>>] MIX COLUMNS")
	mixMatrix = [[2, 3, 1, 1],
				 [1, 2, 3, 1],
				 [1, 1, 2, 3],
				 [3, 1, 1, 2]]
	
	newEstado = [[0 for i in range(4)] for j in range(4)]
	for i in range(4):
		for j in range(4):
			newEstado[i][j] = 0
			for k in range(4):
				if mixMatrix[i][k] == 1:
					newEstado[i][j] ^= estado[k][j]
				elif mixMatrix[i][k] == 2:
				 	newEstado[i][j] ^= xtime(estado[k][j])
				elif mixMatrix[i][k] == 3:
				 	newEstado[i][j] ^= (estado[k][j] ^ xtime(estado[k][j]))
	print(" [?] ESTADO:\n{}".format(np.matrix(hexMatrix(newEstado))))
	return newEstado


def main():
	#sBox = initSBox(16)
	#estado = initEstado(16)
	#print(" [?] ESTADO:\n{}".format(np.matrix(estado)))
	#estado = subBytes(estado, sBox)
	#estado = shiftRows(estado)
	estado = mixColumns([[0x87, 0xf2, 0x4d, 0x97],
						 [0x6e, 0x4c, 0x90, 0xec],
						 [0x46, 0xe7, 0x4a, 0xc3],
						 [0xa6, 0x8c, 0xd8, 0x95]])
	

if __name__ == '__main__':
	main()