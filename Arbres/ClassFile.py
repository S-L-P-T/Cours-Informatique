# -*- coding: utf-8 -*-
"""

classe Pile contenant :
		tete : tete de pile
		methodes :
			push(val) : empile val
			pop() : depile et renvoie la valeur
			__str__ : permet le print de l'objet

"""

from ClassCellule import Cellule

class File:

	def __init__(self):
		self.__tete = None
		self.__queue = None

	def __del__(self): # methode invoquee avant la suppression de l'objet
		while self.__tete != None:
			self.pop()

	def vide(self):
		return self.__queue == None

	def push(self, val):
		nouveau = Cellule(val,None)
		if self.__queue == None:
			self.__tete = nouveau
		else:
			self.__queue.suiv = nouveau
		self.__queue = nouveau

	def pop(self):
		if self.__tete == None:
			return None
		val = self.__tete.val
		self.__tete = self.__tete.suiv
		if self.__tete == None:
			self.__queue = None
		return val

	def __str__(self):
		chaine = "File : \n"
		cursor = self.__tete
		if cursor == None:
			chaine += "Vide"
		while cursor != None:
			chaine += str(cursor) + '\n'
			cursor = cursor.suiv
		return chaine
