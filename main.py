from AES import *

def main():
	print(" [i] Insira um texto de até 8 caracteres: ")
	texto = input()
	print(" [i] Insira uma chave de até 8 caracteres: ")
	chave = input()
	aes = AES64(plaintxt=texto[:8], key=chave[:8]) 
	aes.runAES64()

if __name__ == '__main__':
	main()