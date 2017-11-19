import numpy as np
from util import *
import math as mt
import copy
import random as rnd 

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
			newEstado[i][j] = sBox[int(estado[i][j], 16)]
	print(" [?] ESTADO: {}".format(newEstado))
	return newEstado

def shiftRows(sBox):
	print(" [>>>] SHIFT ROWS")
	newEstado = []
	for i in range(len(sBox)):
		newEstado.append(rotateList(sBox[i], i))
	print(" [?] ESTADO: {}".format(newEstado))
	return newEstado


def mixColumns():
	()

def main():
	sBox = initSBox(16)
	estado = initEstado(16)
	print(" [?] ESTADO: {}".format(estado))
	estado = subBytes(estado, sBox)
	estado = shiftRows(estado)
	
	

if __name__ == '__main__':
	main()