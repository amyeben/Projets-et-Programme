#!/usr/bin/env python
# coding: utf-8


from tkinter import*
from random import*


TAILLE, NB = 500, 7
CHANGE = False
BT_TXT = ["Démarrer","Arrêter"]


def colAlea():
    color="#"
    L=["0", "1", "2" ,"3" ,"4" ,"5" ,"6" ,"7", "8", "9", "a", "b", "c", "d", "e", "f"]
    for i in range(6):
        color += choice(L)        
    return(color)


def changer():
    global CHANGE
    CHANGE = not(CHANGE)
    bt.config(text=BT_TXT[CHANGE])
    changerC()
    return


def changerC():
    for i in range(10):
        can.itemconfig(CARRES[randint(0, len(CARRES)-1)], fill=colAlea())
        can.itemconfig(RONDS[randint(0, len(RONDS)-1)], fill=colAlea())
    if CHANGE:
        fen.after(200, changerC)
    return

    
def dessiner():
    global CARRES, RONDS
    NB = eval(nb.get())
    COT = TAILLE//NB
    MG = COT//10
    CARRES = []
    RONDS = []
    can.delete(ALL) 
    for i in range(NB):
        for j in range(NB):
            CARRES.append(can.create_rectangle(COT*i, COT*j, COT*(i+1), COT*(j+1), fill=colAlea(), width=0))
            RONDS.append(can.create_oval(COT*i+MG, COT*j+MG, COT*(i+1)-MG, COT*(j+1)-MG, fill=colAlea(), width=0))
    return


fen=Tk()
can=Canvas(fen, width=TAILLE, height=TAILLE)
can.pack(side="right")

cadre = Frame(fen)
cadre.pack()
Label(cadre, text="Nb :").pack(side="left")

nb=StringVar()
nb.set(str(NB))
Entry(cadre, textvariable=nb, width=3).pack(side="left")
Button(fen, text="Dessiner", width=20, command=dessiner).pack()

bt=Button(fen, text="Changer couleurs", width= 20,command=changer)
bt.pack()

dessiner()
fen.mainloop()
