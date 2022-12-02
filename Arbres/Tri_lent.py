# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 09:11:40 2022

@author: ocean
"""

from ClassListe import Liste
from ClassArbre import Arbre
from random import randint
from time import time
from tri_fusion import tri_fusion
from tri_fusion import fusion

def creerliste(x):
	liste = []
	for i in range(x):
		y = randint(0, 100)
		liste.append(y)
	return liste


def TriSelec (t) :
	if len (t) == 0 or len (t) == 1 :
		print (t)
		return t
	else :
		for i in range(len(t)):
			for j in range (i, len(t)):
				if t[i] > t[j] :
					temp = t[i]
					t[i] = t[j]
					t[j]= temp
		print (t)
		return t

#tab = [0, 2, 1, 5, 4]
#TriSelec (tab)

def TriInser (t):
	if len (t)==0 or len(t)==1 :
		print (t)
		return t
	else :
		for i in range (1, len(t)):
			k = t[i]
			j = i-1
			while j >=0 and k<t[j]:
				t[j+1] = t[j]
				j= j-1
				t[j+1] = k
	print (t)
	return t


tab = [0, 2, 1, 5, 4, 28, 17, 70]
#TriInser (tab)

l = Liste ()



def TriListe (t):
	if len (t)==0 or len(t)==1 :
		print (t)
		return t
	else :
		for i in range (len(t)):
			l.push (t[i])
	return l

tab = [3, 2, 1, 5, 4, 28, 17, 70]
#TriListe (tab)


"""def TriAbres (t):
	if len (t)==0 or len(t)==1 :
		print (t)
		return t
	else :
		a = Arbre (t[0])
		print ("init")
		for i in range (1,len (t)):
			if t[i]>=t[i-1]:
				Recc (t[i], a.fd)
				print ("grand")
			else :
				Recc (t[i], a.fg)
				print ("petit")
	print (a.parcoursInfixe())
	return a

def Recc (x,b):
	if b == None:
		b = Arbre(x)
		return b
	else :
		if x >= b:
			Recc (x,b.fd)
		else :
			Recc (x, b.fg)"""


def TriAbresF (t):
	if len (t)==0 or len(t)==1 :
		print (t)
		return t
	else :
		a = Arbre (t[0])
		print ("init")
		for i in range (1,len(t)):
			Inser (a, t[i])
			"""if t[i] >= t[i-1]:
				Inser (a, t[i])
				print ("grand")
			else :
				Inser (a, t[i])
				print ("petit")"""
	print (a.parcoursInfixe())
	return a

def Inser (a,e):
	if a == None:
		a = Arbre(e)
		return a
	else :
		if e >= a.val :
			a.fd = Inser (a.fd, e)
		else :
			a.fg = Inser (a.fg, e)
		return a


print (TriAbresF(tab))
"""
def Comparaison(t):
	start = time()
	TriInser(t)
	temps = time() - start
	start2 = time()
	TriListe(t)
	temps2 = time() - start2
	start3 = time()
	TriAbresF(t)
	temps3 = time() - start3
	return temps, temps2, temps3
"""
def tpsInsert(t):
	start = time()
	TriInser(t)
	temps = time() - start
	return temps

def tpsList(t):
	start = time()
	TriListe(t)
	temps = time() - start
	return temps

def tpsArbre(t):
	start = time()
	TriAbresF(t)
	temps = time() - start
	return temps

#print(Comparaison(tab))

def Comparaison2(t, x):
	moyenne1 = 0
	moyenne2 = 0
	moyenne3 = 0
	for i in range(x):
		start = time()
		TriInser(t)
		temps = time()-start
		print(temps)
		moyenne1 += temps
	moyenne1 /= 10
	for j in range(x):
		start = time()
		TriListe(t)
		temps = time()-start
		print(temps)
		moyenne2+=temps
	moyenne2/=10
	for k in range(x):
		start = time()
		TriAbresF(t)
		temps = time()-start
		print(temps)
		moyenne3+=temps
	moyenne3/=10
	return moyenne1, moyenne2, moyenne3

#print(Comparaison2(tab))

def dico(t, x):
	Dico = {}
	l1 =[]
	l2 = []
	l3 = []
	for i in range(x):
		val = tpsInsert(t)
		l1.append(val)
	for j in range(x):
		val = tpsList(t)
		l2.append(val)
	for k in range(x):
		val = tpsArbre(t)
		l3.append(val)
	Dico["Tri par Insertion tps"] = l1
	Dico["Tri par Liste tps"] = l2
	Dico["Tri par Arbre tps"] = l3
	return Dico

#print(dico(tab))


def final():
	x = int(input("Choisi la taille de la liste : "))
	y = int(input("Choisi nombre itération : "))
	tab = creerliste(x)
	r1 = dico(tab, y)
	r2 = Comparaison2(tab, y)
	return "Dictionnaire:",  r1, "Comparaison", r2

l1 =creerliste(10)
l2 =creerliste(10)
print(tri_fusion(fusion(l1,l2)))
"""
print("Par Insertion :", TriInser(tab))
print("Par Liste chainé :", TriListe(tab))
print("Par Arbres :", TriAbresF(tab))
"""
print(final())
