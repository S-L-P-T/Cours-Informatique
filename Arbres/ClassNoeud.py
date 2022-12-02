# -*- coding: utf-8 -*-
"""

Classe Arbre contenant :
	val : la valeur
	fg : reference du fils gauche
	fd : reference du fils droit
	nb : attribut de classe contenant le nombre d'objets
	methodes :
		getter et setter (pas de setter pour nb)
			==> on peut utiliser directement noeud.fg et noeud.fg()
		__str__ : permet le print de l'objet

"""


class Noeud:
	__nb = 0  # compteur de cellules, attribut de classe

	def __init__(self, val, fg = None, fd = None):
		self.__val = val
		self.__fg = fg
		self.__fd = fd
		Noeud.__nb += 1

	def __del__(self): # methode invoquee avant la suppression de l'objet
		Noeud.__nb -= 1

	@property
	def val(self):
		return self.__val

	@val.setter
	def val(self, val):
		self.__val = val

	@property
	def fg(self):
		return self.__fg

	@fg.setter
	def fg(self, fg):
		self.__fg = fg

	@property
	def fd(self):
		return self.__fd

	@fd.setter
	def fd(self, fd):
		self.__fd = fd

	@classmethod
	def nb(cls):
		return Noeud.__nb

	def __str__(self):
		chaine = "val=" + str(self.__val) + " fg="
		if self.__fg == None:
			chaine += "None"  + " fd="
		else:
			chaine += str(id(self.__fg))  + " fd="
		if self.__fd == None:
			chaine += "None"
		else:
			chaine += str(id(self.__fd)) # recupere l'adresse de l'objet et la met en string
		chaine += " nb=" + str(self.__nb)
		return chaine
