#!/usr/bin/env python
# coding: utf-8

from tkinter import*
import random
from random import randint, choice

def deplacement():
    global dx, dy
    if can.coords(balle_rebondissante)[3]>400:
        dy=-1*dy
    if can.coords(balle_rebondissante)[3]<=75:
        dy=5
    if can.coords(balle_rebondissante)[0]<=0:
        dx=-1*dx
    if can.coords(balle_rebondissante)[2]>500:
        dx=-5
    can.move(balle_rebondissante,dx,dy)
    fen.after(30,deplacement)

def couleur_balle():
    clr = '#'
    L=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    for x in range(6):
        clr = clr + random.choice(L)
    return clr
 
dx=5
dy=5

fen = Tk()
can = Canvas(fen,width = 500, height = 400 , bd=0, bg="white")
can.pack(padx=10,pady=10)

Bouton_Quitter=Button(fen, text ='Quitter', command = fen.destroy)
Bouton_Quitter.pack()

Bouton_changecouleur=Button(fen, text ='Changer de couleur', command = couleur_balle())
Bouton_changecouleur.pack()

balle_rebondissante = can.create_oval(25,100,100,25,fill=couleur_balle())
couleur_balle()
deplacement()
fen.mainloop()