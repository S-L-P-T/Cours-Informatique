# -*- coding: utf-8 -*-
"""

classe Liste contenant :
	tete : tete de liste
	methodes :
		push(val) : insertion triee de val dans la liste
		pop(val) : suppression de val de la liste (retourne si element supp ou pas)
		recherche(val) : renvoie la reference de l'objet ou None s'il n'existe pas
		__str__ : permet le print de l'objet

PS : les doublons ne sont pas traites

"""

from ClassCellule import Cellule

class Liste:

	def tete(self):
		return self.__tete.val

	def __init__(self):
		self.__tete = None

	def __del__(self): # methode invoquee avant la suppression de l'objet
		while self.__tete != None:
			self.__tete = self.__tete.suiv

	def vide(self):
		return self.__tete == None

	def push(self, val):
		if self.__tete == None: # liste vide
			self.__tete = Cellule(val, None)
		elif self.__tete.val > val: # insertion en tete
					nouveau = Cellule(val, self.__tete)
					self.__tete = nouveau
		else: # insertion en bonne position : il faut se positionner un cran avant
			cursor = self.__tete
			while cursor.suiv != None and cursor.suiv.val < val:
				cursor = cursor.suiv
			nouveau = Cellule(val, cursor.suiv)
			cursor.suiv = nouveau

	def pop(self, val):
		if self.__tete == None:
			return False
		elif self.__tete.val == val: # supp premier element
			self.__tete = self.__tete.suiv
			return True
		else:
			cursor = self.__tete
			while cursor.suiv != None and cursor.suiv.val != val:
				cursor = cursor.suiv
			if cursor.suiv != None: # si trouve suppression du chainage
				cursor.suiv = cursor.suiv.suiv
				return True
			return False

	def recherche(self, val):
		cursor = self.__tete
		while cursor != None and cursor.val != val:
			cursor = cursor.suiv
		return cursor

	def __str__(self):
		chaine = "Liste : \n"
		cursor = self.__tete
		if cursor == None:
			chaine += "Vide"
		while cursor != None:
			chaine += str(cursor) + '\n'
			cursor = cursor.suiv
		return chaine
