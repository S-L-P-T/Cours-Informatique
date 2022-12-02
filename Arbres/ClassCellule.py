# -*- coding: utf-8 -*-
"""

Classe Cellule contenant :
	val : la valeur
	suiv : reference du suivant
	nb : attribut de classe contenant le nombre d'objets
	methodes :
		getter et setter (pas de setter pour nb)
		__str__ : permet le print de l'objet

"""


class Cellule:
	__nb = 0  # compteur de cellules, attribut de classe

	def __init__(self, val, suiv):
		self.__val = val
		self.__suiv = suiv
		Cellule.__nb += 1

	def __del__(self): # methode invoquee avant la suppression de l'objet
		Cellule.__nb -= 1

	@property
	def val(self):
		return self.__val

	@val.setter
	def x(self, val):
		self.__val = val

	@property
	def suiv(self):
		return self.__suiv

	@suiv.setter
	def suiv(self, suiv):
		self.__suiv = suiv

	@classmethod
	def nb(cls):
		return Cellule.__nb

	def __str__(self):
		chaine = "valeur=" + str(self.__val) + " suivant="
		if self.__suiv == None:
			chaine += "None"
		else:
			chaine += str(id(self.__suiv)) # recupere l'adresse de l'objet et la met en string
		chaine += " nb=" + str(self.__nb)
		return chaine
