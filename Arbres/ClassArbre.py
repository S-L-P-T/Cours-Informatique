# -*- coding: utf-8 -*-
"""
Classe Cellule contenant :
	val : la valeur
	fg : reference du fils gauche
	fd : reference du fils droit
	nb : attribut de classe contenant le nombre d'objets
	methodes :
		getter et setter (pas de setter pour nb)
			==> on peut utiliser directement noeud.fg et noeud.fg()
		__str__ : permet le print de l'objet

"""

from ClassFile import File

class Arbre:

	ELEMENTNULL = -1

	__nb = 0  # compteur de cellules, attribut de classe

	# les fils sont par defaut a None
	def __init__(self, val, fg = None, fd = None):
		self.__val = val
		self.__fg = fg
		self.__fd = fd
		Arbre.__nb += 1


	@property
	def val(self):
		return self.__val

	@val.setter
	def val(self, val):
		self.__val = val

	@property
	def fg(self):
		return self.__fg

	# Definit le fils gauche comme l'arbre passe en parametre
	@fg.setter
	def fg(self, fg):
		if not self.__fg :
			self.__fg = fg

	# Cree le fils gauche de l'arbre
	def ajouterFilsGauche(self, val):
		if self.__fg != None :
			return self.__fg
		else :
			self.__fg = val

	@property
	def fd(self):
		return self.__fd

	# Definit le fils droit comme l'arbre passe en parametre
	@fd.setter
	def fd(self, fd):
		if not self.__fd :
			self.__fd = fd

	# Cree le fils droit de l'arbre
	def ajouterFilsDroit(self, val):
		if self.__fd != None :
			return self.__fd
		else :
			self.__fd = val


	@classmethod
	def nb(cls):
		return Arbre.__nb

	def estVide(self):
		return Arbre.__nb == None

	def estFeuille(self):
		return self.__fg == None and self.__fd == None

	def getRacine(self):
		if Arbre.__nb == 0 :
			return Arbre.__nb.val

	def existeFilsGauche(self):
		return self.__fg != None

	def existeFilsDroit(self):
		return self.__fd != None

	def supprimerFilsGauche(self):
		if self.__fg != None :
			if self.__fg.existeFilsGauche() != None :
				self.__fg.suppimerFilsGauche (self.__fg.existeFilsGauche())
			if self.__fg.existeFilsDroit () != None :
				self.__fg.supprimerFilsDroit(self.__fg.existeFilsDroit ())
			self.__fg = None
		return self


	def supprimerFilsDroit(self):
		if self.__fd != None :
			if self.__fd.existeFilsGauche() != None :
				self.__fd.suppimerFilsGauche (self.__fd.existeFilsGauche())
			if self.__fd.existeFilsDroit () != None :
				self.__fd.suppimerFilsDroit(self.__fd.existeFilsDroit ())
			self.__fd = None
		return self


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


	def parcoursPrefixe(self):
		if self == None:
			return
		print (self.__val, end =',')
		if self.__fg != None :
			self.__fg.parcoursPrefixe ()
		if self.__fd != None :
			self.__fd.parcoursPrefixe ()



	def parcoursInfixe(self):
		if self == None :
			return
		if self.__fg != None :
			self.__fg.parcoursInfixe ()
		print (self.__val, end =',')
		if self.__fd != None :
			self.__fd.parcoursInfixe ()


	def parcoursSuffixe(self):
		if self == None :
			return
		if self.__fg != None :
			self.__fg.parcoursSuffixe ()
		if self.__fd != None :
			self.__fd.parcoursSuffixe ()
		print (self.__val, end = ',')


	def parcoursLargeur(self):
		if self != None :
			f = File
			f.push (f, self)
		while f != None :
			noeud = f.pop()
			print (f.getRacine())
			if f.existeFilsGauche (noeud):
				f.push (noeud.__fg)
			if f.existeFilsDroit (noeud) :
				f.push (noeud.__fd)
