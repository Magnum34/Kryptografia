#!/usr/bin/env python

#text = '1101110010011110'
text = '1110000111000011'
key = '0001110010010010'
text = list(text)
size_text = len(text)
key = list(key)

matrix_text = []
matrix_key = []
t = 0
for i in range(4):
	matrix_text.append(text[0+t:4+t])
	t += 4
t = 0
for i in range(4):
	matrix_key.append(key[0+t:4+t])
	t += 4

SboxE={(0,0,0,0):[1,1,1,0],
       (0,0,0,1):[0,1,0,0],
       (0,0,1,0):[1,1,0,1],
       (0,0,1,1):[0,0,0,1],
       (0,1,0,0):[0,0,1,0],
       (0,1,0,1):[1,1,1,1],
       (0,1,1,0):[1,0,1,1],
       (0,1,1,1):[1,0,0,0],
       (1,0,0,0):[0,0,1,1],
       (1,0,0,1):[1,0,1,0],
       (1,0,1,0):[0,1,1,0],
       (1,0,1,1):[1,1,0,0],
       (1,1,0,0):[0,1,0,1],
       (1,1,0,1):[1,0,0,1],
       (1,1,1,0):[0,0,0,0],
       (1,1,1,1):[0,1,1,1]
       
       }
SboxD={(0,0,0,0):[1,1,1,0],
       (0,0,0,1):[0,0,1,1],
       (0,0,1,0):[0,1,0,0],
       (0,0,1,1):[1,0,0,0],
       (0,1,0,0):[0,0,0,1],
       (0,1,0,1):[1,1,0,0],
       (0,1,1,0):[1,0,1,0],
       (0,1,1,1):[1,1,1,1],
       (1,0,0,0):[0,1,1,1],
       (1,0,0,1):[1,1,0,1],
       (1,0,1,0):[1,0,0,1],
       (1,0,1,1):[0,1,1,0],
       (1,1,0,0):[1,0,1,1],
       (1,1,0,1):[0,0,1,0],
       (1,1,1,0):[0,0,0,0],
       (1,1,1,1):[0,1,0,1]
       
       }
tmp_1 = []
tmp_2 = []
t = 0	
for i in range(4):
	for j in range(4):
		tmp_1.append(int(matrix_key[i][j]))
	tmp_2.append(tmp_1[0+t:4+t])
	t += 4
matrix_key = []
matrix_key = tmp_2
        
def Roundkey(key ,n):
	key_rund = []
	key_rund_1 = []
	box = SboxE[tuple(key[3])]
	print "klucz sboxE: %s"%(box)
	tab = [0,0,0,1]
	tab1 = [0,0,1,0]
	if n == 1:
		for i in range(4):
			key_rund.append(key[0][i] ^ box[i] ^ tab[i])
		key_rund_1.append(key_rund)
		key_rund = []
		for i in range(4):
			key_rund.append(key[2][i] ^ key_rund_1[0][i] )
		key_rund_1.append(key_rund)
		key_rund = []
		for i in range(4):
			key_rund.append(key[1][i] ^ key_rund_1[1][i] )
		key_rund_1.append(key_rund)
		key_rund = []
		for i in range(4):
			key_rund.append(key[3][i] ^ key_rund_1[2][i] )
		key_rund_1.append(key_rund)
		tmp = key_rund_1[1]
		key_rund_1[1] = key_rund_1[2]
		key_rund_1[2] = tmp			
		return key_rund_1
	if n == 2:
		for i in range(4):
			key_rund.append(key[0][i] ^ box[i] ^ tab1[i])
		key_rund_1.append(key_rund)
		key_rund = []
		for i in range(4):
			key_rund.append(key[2][i] ^ key_rund_1[0][i] )
		key_rund_1.append(key_rund)
		key_rund = []
		for i in range(4):
			key_rund.append(key[1][i] ^ key_rund_1[1][i] )
		key_rund_1.append(key_rund)
		key_rund = []
		for i in range(4):
			key_rund.append(key[3][i] ^ key_rund_1[2][i] )
		key_rund_1.append(key_rund)
		tmp = key_rund_1[1]
		key_rund_1[1] = key_rund_1[2]
		key_rund_1[2] = tmp			
		return key_rund_1
	
#SubBytes
def subBytes(matrix_text):
	for i in range(4):
		matrix_text[i] = SboxE[tuple(matrix_text[i])]
	return matrix_text
def subBytesDesz(matrix_text):
	for i in range(4):
		matrix_text[i] = SboxD[tuple(matrix_text[i])]
	return matrix_text	
#Shiftrows
def Shiftrows(matrix_text):
	tmp = []
	tmp = matrix_text[2]
	matrix_text[2] = matrix_text[3]
	matrix_text[3] = tmp
	return matrix_text
#Mnozenie binarne 
def mn_binar(w1,w2):
	mnsum = []
	i =3
	while 0 <= i:
		mn = []
		for j in range(4):
			mn.append(w1[j]*w2[i])
		if 0 < i:
			for k in range(i):
				mn.insert(0,0)
		i = i-1		
		mnsum.append(mn)
	j = 0
	i = 0	
	while i < 4:
		for k in range(i):
			mnsum[j].append(0)		
		i = i+1
		j = j +1
	mn = []	
	for j in range(len(mnsum[0])):
		sm = 0
		for i in range(4):
			sm += mnsum[i][j]
		mn.append(sm)
	
	for i in range(len(mn)):
		mn[i] = mn[i]%2				
	return mn
#Dzielenie binarne
def dziel_bin(dziel):
	const = [1,0,0,1,1]
	m = 0
	while m < 3:
		if dziel[m] == 1:
			tmp = []
			dz = dziel[m]/const[0]
			if 0 < m:
				for i in range(m):
					tmp.append(0)
			for i in range(len(const)):
				tmp.append(dz*const[i])	
			xor = []
			for i in range(len(tmp)):
				xor.append(dziel[i]^tmp[i])
			for i in range(len(tmp),len(dziel)):
				xor.append(dziel[i])
			
			dziel = xor
		m = m+1			
	return dziel
#dodawnie mixcolumns
def mixcolumns_dod(w1,w2):
	w = []
	for i in range(7):
		w.append(w1[i]^w2[i])
	return w	
#mixcolumns
def mixcolums(text):
	const = [[0,0,1,1],[0,0,1,0]]
	w1 = dziel_bin(mn_binar(text[0],const[0]))
#	print "w1 %s"%(mn_binar(text[0],const[0]))
#	print "w1 %s"%(w1)
	w2 = dziel_bin(mn_binar(text[2],const[1]))
#	print "w2 %s"%(mn_binar(text[1],const[1]))
#	print "w2 %s"%(w2)
	w3 = dziel_bin(mn_binar(text[1],const[0]))
#	print text[1]
#	print "w3 %s"%(mn_binar(text[1],const[0]))
#	print "w3 %s"%(w3)
	w4 = dziel_bin(mn_binar(text[3],const[1]))
#	print text[3]
#	print "w4 %s"%(mn_binar(text[3],const[1]))
#	print "w4 %s"%(w4)
	w5 = dziel_bin(mn_binar(text[0],const[1]))
#	print "w5 %s"%(mn_binar(text[2],const[0]))
#	print "w5 %s"%(w5)
	w6 = dziel_bin(mn_binar(text[2],const[0]))
#	print "w6 %s"%(mn_binar(text[3],const[1]))
#	print "w6 %s"%(w6)
	w7 = dziel_bin(mn_binar(text[1],const[1]))
#	print "w7 %s"%(mn_binar(text[2],const[1]))
#	print "w7 %s"%(w7)
	w8 = dziel_bin(mn_binar(text[3],const[0]))
#	print "w8 %s"%(mn_binar(text[3],const[0]))
#	print "w8 %s"%(w8)
	w1_2 = mixcolumns_dod(w1,w2)
#	print "w1_2 %s"%(w1_2)
	w3_4  = mixcolumns_dod(w3,w4)
#	print "w3_4 %s"%(w3_4)
	w5_6  = mixcolumns_dod(w5,w6)
#	print "w5_6 %s"%(w5_6)
	w7_8  = mixcolumns_dod(w7,w8)
#	print "w7_8 %s"%(w7_8)
	m1 = []
	m2 = []
	m3 = []
	m4 = []
	for i in range(3,7):
		m1.append(w1_2[i])
		m2.append(w3_4[i])
		m3.append(w5_6[i])
		m4.append(w7_8[i])
	m = []
	m.append(m1)
	m.append(m2)
	m.append(m3)
	m.append(m4)
	return m
def addround(matrix_text,matrix_key):
	mc = []
	for i in range(4):
		wynik = []
		for j in range(4):
			wynik.append(int(matrix_text[i][j]) ^ int(matrix_key[i][j]))
		mc.append(wynik)		
	return mc 								
#Runda 0
key = matrix_key
print "text %s"%(matrix_text)       
for i in range(4):
	for j in range(4):
		matrix_text[i][j] = int(matrix_text[i][j]) ^ int(matrix_key[i][j]) 	
print "klucz %s"%(matrix_key)
#Runda 1
print "Runda 1"
#Subbytes
matrix_text = subBytes(matrix_text)
print "subBytes %s"%(matrix_text)
#shiftRows
matrix_text = Shiftrows(matrix_text)
print "ShiftRows %s"%(matrix_text)
#Mixcolumns
matrix_text = mixcolums(matrix_text) 
print "Mixcolumns : %s"%(matrix_text)
#Roundkey
matrix_key = Roundkey(matrix_key,1)
key1 = matrix_key
print "klucz1 %s"%(matrix_key)
matrix_text = addround(matrix_text,matrix_key)
print "addround %s"%(matrix_text)
#Runda 2	    
print "Runda 2"
#Subbytes
matrix_text = subBytes(matrix_text)
print "subBytes %s"%(matrix_text)
#shiftRows
matrix_text = Shiftrows(matrix_text)
print "ShiftRows %s"%(matrix_text)
#Roundkey
matrix_key = Roundkey(matrix_key,2)
key2 = matrix_key
print "klucz2 %s"%(matrix_key)
matrix_text = addround(matrix_text,matrix_key)
print "addround %s"%(matrix_text)

#Deszyfrowanie
print "Deszyfrowanie "
#runda 0
print "Runda 0"
#Roundkey
print "klucz2 %s"%(key2)
matrix_text = addround(matrix_text,key2)
print "addround %s"%(matrix_text)
#shiftRows
matrix_text = Shiftrows(matrix_text)
print "ShiftRows %s"%(matrix_text)
#Subbytes
matrix_text = subBytesDesz(matrix_text)
print "subBytes %s"%(matrix_text)
#runda 1
print "Runda 1"
#Roundkey
print "klucz1 %s"%(key1)
matrix_text = addround(matrix_text,key1)
print "addround %s"%(matrix_text)
#Mixcolumns
matrix_text = mixcolums(matrix_text) 
print "Mixcolumns : %s"%(matrix_text)
#shiftRows
matrix_text = Shiftrows(matrix_text)
print "ShiftRows %s"%(matrix_text)
#Subbytes
matrix_text = subBytesDesz(matrix_text)
print "subBytes %s"%(matrix_text)
#Roundkey
print "Runda 2"
print "klucz %s"%(key)
wynik = addround(matrix_text,key)
print "odszyfrowane %s"%(wynik)
