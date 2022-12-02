# -*- coding: utf-8 -*-
"""

Programme principal contenant les tests des classes

"""


from ClassArbre import Arbre

def testAB():
	a = Arbre(1)
	print(a)
	a.fg = Arbre(2)
	a.fd = Arbre(3)
	print(a)
	p = a.fg
	print(p)
	p.fg = Arbre(4)
	p.fd = Arbre(5)
	p = a.fd
	p.fg = Arbre(6)
	p.fd = Arbre(7)
	p = a.fg.fg
	p.fg = Arbre(8)
	p.fd = Arbre(9)
	p = a.fg.fd
	p.fg = Arbre(10)
	p.fd = Arbre(11)
	p = a.fd.fg
	p.fg = Arbre(12)
	p.fd = Arbre(13)
	p = a.fd.fd
	p.fg = Arbre(14)
	p.fd = Arbre(15)
	a.parcoursPrefixe()
	print("")
	a.parcoursInfixe()
	print("")
	a.parcoursSuffixe()
	print("")
	a.parcoursLargeur()
	print("")


testAB()
