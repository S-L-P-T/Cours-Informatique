# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 09:28:01 2022

@author: Matthys
"""

import tkinter as tk
import tkinter.ttk as ttk

class DemoWidget(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.champs = {
            'nombre': tk.StringVar()
        }
        self._create_gui()
        self.pack()

    def _create_gui(self):
        label = tk.Label(self, text="Les différents types de tri")
        label.grid(column=0, row=0, columnspan=3)

        label = tk.Label(self, text="")
        label.grid(column=0, row=1)

        label = tk.Label(self, text="Entrez un nombre :")
        label.grid(column=0, row=2)

        text = tk.Entry(self, textvariable=self.champs['nombre'])
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

        label = tk.Label(self, text="© Ariana Sauvant, Matthys Tachon-Panafieu, Benjamin Corral, Sahnoune Samy")
        label.grid(column=0, row=15, columnspan=3)

    def valider(self):
        """affiche les valeurs saisies sur la console
            mais on pourrait faire quelque chose de plus intéressant"""
        for v, k in self.champs.items():
            print(f"{v} : {k.get()}")
            nombre = k.get()
            print(nombre)
            


app = tk.Tk()
app.title("Les différents types de tri")
app.geometry("450x350")
DemoWidget(app)
app.mainloop()