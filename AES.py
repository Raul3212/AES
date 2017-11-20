from util import *
import math as mt
import copy

mixMatrix = [
	[2, 3, 1, 1],
	[1, 2, 3, 1],
	[1, 1, 2, 3],
	[3, 1, 1, 2]
]

sBox = (
	0b0000, 0b0001, 0b1001, 0b1110, 
	0b1101, 0b1011, 0b0111, 0b0110,
	0b1111, 0b0010, 0b1100, 0b0101,
	0b1010, 0b0100, 0b0011, 0b1000, 
)

RC = (0b0001, 0b0010, 0b0100, 0b1000, 0b0011, 0b0110, 0b1100, 0b1011, 0b0101, 0b1010)

# Regra da multiplicação para 64 bits
xtime = lambda a: (((a << 1) ^ 0x3) & 0xF) if (a & 0x8) else (a << 1)

class AES64:
	global sBox
	global RC
	global mixMatrix
	#key: string com 8 caracteres (8 bytes ou 64 bits)
	def __init__(self, plaintxt, key):
		self.__estado = self.__texto2Estado(plaintxt)
		self.__key = key

	def __subBytes(self):
		for i in range(4):
			for j in range(4):
				self.__estado[i][j] = sBox[self.__estado[i][j]]
		
	def __shiftRows(self):
		for i in range(len(self.__estado)):
			self.__estado[i] = rotateList(self.__estado[i], i)

	def __mixColumns(self):
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

	
	def __keyExpasion(self):
		indexLinha = 0
		indexColuna = 0
		proxIndexLinha = False
		w = [[0 for i in range(4)] for j in range(44)]
		for x in self.__key:
			bin1Byte = format(ord(x), '08b')
			f4Bits, s4Bits = bin1Byte[:(int(len(bin1Byte)/2))], bin1Byte[int((len(bin1Byte)/2)):]
			w[indexLinha][indexColuna] = int(f4Bits, 2)
			w[indexLinha][indexColuna+1] = int(s4Bits, 2)
			indexColuna += 2
			if indexColuna == 4:
				indexColuna = 0
			if proxIndexLinha == True:
				indexLinha += 1
			proxIndexLinha = not proxIndexLinha

		for i in range(4, 44):
			temp = w[i - 1]
			if i % 4 == 0:
				temp = xorList(self.__subWord(rotateList(temp, 1)), self.__Rcon(int((i/4)-1)))
			w[i] = xorList(w[i-4], temp)

		self.__chavesRodada = []
		for i in range(0,44,4):
			subChave = []
			subChave.append(w[i])
			subChave.append(w[i+1])
			subChave.append(w[i+2])
			subChave.append(w[i+3])
			self.__chavesRodada.append(subChave)

	#usada na expansao da chave
	def __subWord(self, lista):
		newLista = copy.copy(lista)
		for i in range(len(lista)):
				newLista[i] = sBox[lista[i]]
		return newLista

	def __Rcon(self, index):
		#tem q ser calculada usando o polinomio 
		
		return [RC[index], 0, 0, 0]

	def __addRoundKey(self, rodada):
		self.__estado = xorKey(self.__estado, self.__chavesRodada[rodada])

	def __texto2Estado(self, texto):
		indexLinha = 0
		indexColuna = 0
		proxIndexLinha = False
		estado = [[0 for i in range(4)] for j in range(4)]
		for x in texto:
			bin1Byte = format(ord(x), '08b')
			f4Bits, s4Bits = bin1Byte[:(int(len(bin1Byte)/2))], bin1Byte[int((len(bin1Byte)/2)):]
			estado[indexLinha][indexColuna] = int(f4Bits, 2)
			estado[indexLinha][indexColuna+1] = int(s4Bits, 2)
			indexColuna += 2
			if indexColuna == 4:
				indexColuna = 0
			if proxIndexLinha == True:
				indexLinha += 1
			proxIndexLinha = not proxIndexLinha
		return estado

	def __estado2texto(self, estado):
		texto = ""
		for i in range(4):
			for j in range(0,4,2):
				fbin4bits = format(estado[i][j], '04b')
				sbin4bits = format(estado[i][j+1], '04b')
				total1Byte = fbin4bits + sbin4bits
				caracter = str(chr(int(total1Byte, 2)))
				texto = texto + caracter
		return texto

	def runAES64(self):
		self.__keyExpasion()
		self.__addRoundKey(0)
		for rodada in range(10):
			print(" [->] RODADA {}".format(rodada))
			print(" [>>] SubBytes...")
			self.__subBytes()
			print(" [>>] ShiftRows...")
			self.__shiftRows()
			if rodada < 9:
				print(" [>>] MixColumns...")
				self.__mixColumns()
			print(" [>>] Add RoundKey...")
			self.__addRoundKey(rodada+1)
		print("ESTADO FINAL:\n{}".format(self.__estado))
		print("TEXTO FINAL:\n{}".format(self.__estado2texto(self.__estado)))