#!/usr/bin/env python
# coding: utf-8

from tkinter import*
import random
from random import randint, choice
N=int(input("Entrez le nombre de case"))

def couleur_alea():
    clr = '#'
    L=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    for i in range(6):
        clr = clr + choice(L)
    return clr

def button_change_couleur():
    button_change_couleur.bind(randint.couleur_alea)

def carre(N):
    for i in range(N):
        for j in range(N):

            couleurA=couleur_alea()
            posit = (i*50,j*50,(i+1)*50,(j+1)*50)
            can.create_rectangle(posit, fill = couleurA)

            couleurB = couleur_alea()
            can.create_oval(i*50+5,j*50+5,(i+1)*50-5,(j+1)*50-5, fill =couleurB)

fen = Tk()
can = Canvas(fen, width=1000, height=1000)
Bouton1 = Button(fen, text = 'Quitter', command = fen.destroy)
Bouton1.pack()
Bouton2 = Button(fen, text = 'Changez de couleur', command = button_change_couleur)
Bouton2.pack()
can.pack()
carre(N)
fen.mainloop()


print(couleur_alea())