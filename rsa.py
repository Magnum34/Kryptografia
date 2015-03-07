#!/usr/bin/env python
#-*- coding: utf-8-*-
import random

def pot_mod(a,k,n):
	k_bin = bin(k)
	size = len(k_bin)
	k_bin = k_bin[2:size]
	size = len(k_bin)
	potega = []
	i = size-1
	while 0 <= i:
		potega.append(pow(2,i))
		i = i -1
	reszta = []
	for i in range(size):
		reszta.append(pow(a,potega[i])%n)
	suma = 1
	for i in range(size):
		if int(k_bin[i]) == 1:
			suma *= reszta[i]	
	return suma%n
def sito(n):
	p = [2,3,5,7]
	for i in range(2,n):	
		if (i%2 <> 0 ) and (i%3 <> 0)and ( i%5 <> 0) and( i%7 <> 0) :
			p.append(i)
	return p
def euklides(a,b):	
	r = 1
	while r <> 0:
		r = a%b
		a = b
		b = r
	return a
def rosz_eklides(a,b):
	q = a/b
	r = a%b
	x0 = 1
	x1 = 0
	y0 = 0
	y1 = 1
	while r <> 0:
		x_tmp = x1
		y_tmp = y1
		x1 =x0-q*x1
		y1= y0 -q*y1
		x0 = x_tmp
		y0 = y_tmp
		a = b
		b = r
		q = a/b
		r = a%b
	return x1
	
print euklides(8,4)				
print "#Sito Eratostenesa#"
n = input("n = ")
print sito(n)
print "#Algorytm Eklidesa#"
print "NWD(a,b)"
a = input("a = " )
b = input("b = ")
print euklides(a,b)
print "#Roszerzony algorytm Eklidesa#"
print "NWD(a,b)"
a = input("a = " )
b = input("b = ")
q = a/b
r = a%b
x0 = 1
x1 = 0
y0 = 0
y1 = 1
print "a = %d  q = - x = 1 y = 0"%(a)
print "b = %d  q = - x = 0 y = 1"%(b)
while r <> 0:
	x_tmp = x1
	y_tmp = y1
	x1 =x0-q*x1
	y1= y0 -q*y1
	x0 = x_tmp
	y0 = y_tmp
	print "r = %d  q = %d x = %d y = %d"%(r,q,x1,y1) 
	a = b
	b = r
	q = a/b
	r = a%b
print "#Szyfr RSA#"
print "Do ilu będzie wygenerowanych liczb pierwszych przy wylosowaniu P i Q "
n = input("n = ")
tab = sito(n)
#P = random.choice(tab)
#Q = random.choice(tab)
P = 11
Q = 13
print "P = %d"%(P)
print "Q = %d"%(Q)
N = P*Q
fi = (P-1)*(Q-1)
print "fi = %d"%(fi)
for i in range(2,fi-1):
	if euklides(i,fi) == 1:
		e = i
		break
print "e = %d"%(e)
d = rosz_eklides(e,fi) + fi
print "D = %d"%(d)
print "klucz publiczny = (%d,%d)"%(N,e)
print "klucz prywatny = (%d,%d)"%(N,d)
t = input("Wpisujemy liczbe do zaszyfrowania do N-1 = ")
c = pot_mod(t,e,N)
print "szyfrowanie : %d"%(c)
m = pot_mod(c,d,N)
print "Roszyfrowanie : %d"%(m)
