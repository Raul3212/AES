def list2matrix(lista, n):
	matrix = []
	for i in range(0, len(lista), n):
		matrix.append(lista[i:i+n])
	return matrix

def rotateList(lista, n):
	return lista[n:] + lista[0:n]

def text2matrix(text):
    matrix = []
    for i in range(16):
        byte = (text >> (8 * (15 - i))) & 0xFF
        if i % 4 == 0:
            matrix.append([byte])
        else:
            matrix[int(i / 4)].append(byte)
    return matrix