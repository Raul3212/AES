import numpy as np
from util import *
import math as mt
import copy

mixMatrix = [
	[2, 3, 1, 1],
	[1, 2, 3, 1],
	[1, 1, 2, 3],
	[3, 1, 1, 2]
]

# Regra da multiplicação (Eq. 4.14)
xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

class AES64:

	def __init__(self, plaintxt):
		self.__estado = initEstado(16)
		self.__sBox = self.__initSBox(16)

	def __initSBox(self, n):
		sBox = []
		for i in range(n):
			sBox.append(i)
		return sBox

	def __subBytes(self):
		for i in range(4):
			for j in range(4):
				self.__estado[i][j] = self.__sBox[self.__estado[i][j]]
		
	def __shiftRows(self):
		for i in range(len(self.__estado)):
			self.__estado[i] = rotateList(self.__estado[i], i)

	def __mixColumns(self):
		global mixMatrix
		newEstado = [[0 for i in range(4)] for j in range(4)]
		for i in range(4):
			for j in range(4):
				newEstado[i][j] = 0
				for k in range(4):
					if mixMatrix[i][k] == 1:
						newEstado[i][j] ^= self.__estado[k][j]
					elif mixMatrix[i][k] == 2:
					 	newEstado[i][j] ^= xtime(self.__estado[k][j])
					elif mixMatrix[i][k] == 3:
					 	newEstado[i][j] ^= (self.__estado[k][j] ^ xtime(self.__estado[k][j]))
		self.__estado = newEstado

	def runAES64(self):
		self.__subBytes()
		self.__shiftRows()
		self.__mixColumns()
		
		print(self.__estado)

def main():
	aes = AES64(None) 
	aes.runAES64()

if __name__ == '__main__':
	main()