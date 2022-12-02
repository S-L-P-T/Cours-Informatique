# -*- coding: utf-8 -*-
"""

classe File contenant :
		tete : tete de file
		queue : queue de file
		methodes :
			push(val) : enfile val
			pop() : defile et renvoie la valeur
			__str__ : permet le print de l'objet

"""

from ClassCellule import Cellule

class Pile:

	def __init__(self):
		self.__tete = None

	def __del__(self): # methode invoquee avant la suppression de l'objet
		while self.__tete != None:
			self.pop()

	def vide(self):
		return self.__tete == None

	def push(self, val):
		if self.__tete == None:
			self.__tete = Cellule(val, None)
		else:
			nouveau = Cellule(val, self.__tete)
			self.__tete = nouveau
		# self.__tete = Cellule(val, self.__tete) # cela suffit

	def pop(self):
		if self.__tete == None:
			return None
		val = self.__tete.val
		self.__tete = self.__tete.suiv
		return val

	def __str__(self):
		chaine = "Pile : \n"
		cursor = self.__tete
		if cursor == None:
			return chaine + "Vide"
		while cursor != None:
			chaine += str(cursor) + '\n'
			cursor = cursor.suiv
		return chaine
