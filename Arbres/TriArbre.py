# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 09:28:01 2022

@author: Matthys
"""

"""def tri_selection(a):

	if len(a) == 0 or len(a) == 1 :
		print(a)
		return a
	else:
		for i in range(len(a)):
			for j in range(i, len(a)):
				if a[i] > a[j]:
					tmp = a[i]
					a[i] = a[j]
					a[j] = tmp
		print(a)
		return a

tri_selection(a)"""

# def tri_rapide(a):
# 	i=1
# 	while i != len(a) or a[0] > a[i]:
# 		i=i+1
# 	else:
# 		max = a[i]

# 	k = len(a)

# 	while k != 0 or a[0] < a[i]:
# 		k=k-1
# 	else:
# 		min = a[k]
# 		tempo = min

# 	min = max
# 	max = tempo


# 	print(a,min,max)
# 	print(len(a))

# tri_rapide(a)

# a = [27,63,1,72,64,58,14,9]

# def tri_rapide(a):
# 	inf = a[1]
# 	nmb = len(a)
# 	sup = a[nmb]

# 	while inf <= sup:
# 		while (inf <= a[nmb]) and (a[inf] <= a[a[1]]):
# 			inf = inf+1
# 		while (a[sup] > a[a[1]]):
# 			sup = sup-1
# 		if inf < sup:
# 			tmp = a[sup]
# 			a[sup] = a[inf]
# 			a[inf] = tmp
# 	tmp = a[a[1]]
# 	a[a[1]] = a[sup]
# 	a[sup] = tmp

# tri_rapide(a)

# pivot = a[0]
# nmb = len(a)

# def sup():
# 	i = 1
# 	while pivot > a[i] or i != nmb:
# 		i = i+1
# 	return a[i]
	

# def inf():
# 	j = nmb
# 	while pivot < a[j] or j != 1:
# 		j = j-1
# 	return a[j]

# def tri_rapide(a):

# 	while inf <= sup:
# 		while (inf <= a[nmb]) and (a[inf] <= a[a[1]]):
# 			inf = inf+1
# 		while (a[sup] > a[a[1]]):
# 			sup = sup-1
# 		if inf < sup:
# 			tmp = a[sup]
# 			a[sup] = a[inf]
# 			a[inf] = tmp
# 	tmp = a[a[1]]
# 	a[a[1]] = a[sup]
# 	a[sup] = tmp

# tri_rapide(a)
"""
from tkinter import * 

fenetre = Tk()
fenetre.title("Les différents types de tri")
fenetre.geometry("600x600")

def frame(a,b):
	l = LabelFrame(fenetre, text=a, padx=20, pady=20)
	l.pack(fill="both", expand="yes")
 
	Label(l, text=b).pack()

def space():
	space = Label(fenetre, text="\n")
	space.pack()

label = Label(fenetre, text="Les différents types de tri")
label.pack()

space()




  


L1 = Label(fenetre, text="Veuillez rentrer la liste :")
L1.grid(column=0, row=0)
L1.pack()
E1 = Entry(fenetre)
E1.grid(column=1, row=0, columnspan=2)
E1.pack()



space()

frame("Tri par selection","Temps : Tri par selection")
space()
frame("Tri par insertion","Temps : Tri par insertion")
space()
frame("Tri par liste chainée","Temps : Tri par liste chainée")
space()
frame("Tri par arbre","Temps : Tri par arbre")

fenetre.mainloop()
"""

import tkinter as tk
import tkinter.ttk as ttk


class DemoWidget(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.champs = {
            'message': tk.StringVar()
        }
        self._create_gui()
        self.pack()

    def space():
        space = tk.Label(app, text="\n")
        space.pack()

    def frame(a,b):
        l = tk.LabelFrame(app, text=a, padx=20, pady=20)
        l.pack(fill="both", expand="yes")
        tk.Label(l, text=b).pack()

    def _create_gui(self):
        label = tk.Label(self, text="Les différents types de tri")
        label.grid(column=0, row=0, columnspan=3)

        label = tk.Label(self, text="")
        label.grid(column=0, row=1)

        label = tk.Label(self, text="Un message")
        label.grid(column=0, row=2)

        text = tk.Entry(self, textvariable=self.champs['message'])
        text.grid(column=1, row=2, columnspan=2)

        label = tk.Label(self, text="")
        label.grid(column=0, row=3)

        label = tk.Label(self, text="Tri par selection :")
        label.grid(column=0, row=4, sticky=tk.E)

        label = tk.Label(self, text="Temps: Tri par selection")
        label.grid(column=1, row=4, columnspan=2, sticky=tk.W)

        label = tk.Label(self, text="")
        label.grid(column=0, row=5)

        label = tk.Label(self, text="Tri par insertion :")
        label.grid(column=0, row=6, sticky=tk.E)

        label = tk.Label(self, text="Temps: Tri par insertion")
        label.grid(column=1, row=6, columnspan=2, sticky=tk.W)

        label = tk.Label(self, text="")
        label.grid(column=0, row=7)

        label = tk.Label(self, text="Tri par liste chainée :")
        label.grid(column=0, row=8, sticky=tk.E)

        label = tk.Label(self, text="Temps: Tri par liste chainée")
        label.grid(column=1, row=8, columnspan=2, sticky=tk.W)

        label = tk.Label(self, text="")
        label.grid(column=0, row=9)

        label = tk.Label(self, text="Tri par arbre :")
        label.grid(column=0, row=10, sticky=tk.E)

        label = tk.Label(self, text="Temps: Tri par arbre")
        label.grid(column=1, row=10, columnspan=2, sticky=tk.W)

        label = tk.Label(self, text="")
        label.grid(column=0, row=11)

        button = tk.Button(self, text="Valider", command=self.valider)
        button.grid(column=0, row=12)

        button = tk.Button(self, text="Fermer", command=app.quit)
        button.grid(column=2, row=12)

        label = tk.Label(self, text="")
        label.grid(column=0, row=13)
        
        label = tk.Label(self, text="")
        label.grid(column=0, row=14)

        label = tk.Label(self, text="© Ariana Sauvant, Matthys Tachon-Panafieu, Benjamin Corral")
        label.grid(column=0, row=15, columnspan=3)

    def valider(self):
        """affiche les valeurs saisies sur la console
            mais on pourrait faire quelque chose de plus intéressant"""
        for v, k in self.champs.items():
            print(f"{v} : {k.get()}")
            


app = tk.Tk()
app.title("Les différents types de tri")
app.geometry("400x350")
DemoWidget(app)
app.mainloop()