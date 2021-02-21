#!/usr/bin/env python
# coding: utf-8

from tkinter import *
import random
from random import randint, choice

fen = Tk()
fen.title('ACTION OU VERITE')
fen.config(cursor ='top_left_arrow')



def creation_can2():
    can.delete(item)
    b_2 = Button(fen, text = "DEUX JOUEURS", font = 'ArcadeClassic', command = joueur2)
    b_2_ = can.create_window(250,175, window = b_2)
    b_3 = Button(fen, text = "TROIS JOUEURS", font = 'ArcadeClassic', command = joueur3)
    b_3_ = can.create_window(250,250, window = b_3)
    b_4 = Button(fen, text = "QUATRE JOUEURS", font = 'ArcadeClassic', command = joueur4)
    b_4_ = can.create_window(250,325, window = b_4)
    boutton_play.destroy()

def joueur2():
    value1 = StringVar(fen)
    value1.set("Ton pseudo J1")
    value2 = StringVar(fen)
    value2.set("Ton pseudo J2")
    pseudo1 = Entry(fen, textvariable = value1, cursor ='left_ptr')
    can.create_window(175,210, window = pseudo1)
    pseudo2 = Entry(fen, textvariable = value2, cursor ='left_ptr')
    can.create_window(325,210, window = pseudo2)

    def hourglass2():
        can['bg']='beige'
        can.delete('all')
        bouton_action = Button(fen, text = 'ACTION', font = 'Helvetica',width = 20, bg = 'red', relief = 'ridge', cursor ='left_ptr', activebackground = 'white', activeforeground = 'red',command = action2)
        can.create_window(250, 175, window = bouton_action)
        bouton_verite = Button(fen, text = 'VERITE', font = 'Helvetica',width = 20, bg = 'red', relief = 'ridge', cursor ='left_ptr', activebackground = 'white', activeforeground = 'red')
        can.create_window(250, 300, window = bouton_verite)
        w1 ="Alors",pseudo1.get(),",","tu","choisis", "action","ou","vérité","?"
        can.create_text(250,50, text = (w1), fill = 'brown', font = 'Century')
##        w2 = pseudo2.get()
##        can.create_text(340,50, text = w2, fill = 'brown', font = 'Century')

    def action2():
            can.delete('all')
            can['bg']='white'
            with open("action.TXT","r") as fichier:
                liste = fichier.readlines()
            for i in range(len(liste)):
                liste[i]=liste[i].strip()
            for i in range(1):
                q = random.choice(liste)
            print(q)
            w1_ = pseudo1.get(),q
            can.create_text(250,50, text = (w1_), fill = 'brown', font = 'Century 10')

##            lab = action2()
    bouton_validej2 = Button(fen, relief='raised',bitmap="hourglass", command = hourglass2)
    can.create_window(420,210, window = bouton_validej2)



def joueur3():
    value1_ = StringVar(fen)
    value1_.set("Ton pseudo J1")
    value2_ = StringVar(fen)
    value2_.set("Ton pseudo J2")
    value3_ = StringVar(fen)
    value3_.set("Ton pseudo J3")
    pseudo1_ = Entry(fen, textvariable = value1_, cursor ='left_ptr')
    can.create_window(110,290, window = pseudo1_)
    pseudo2_ = Entry(fen, textvariable = value2_, cursor ='left_ptr')
    can.create_window(250,290, window = pseudo2_)
    pseudo3_ = Entry(fen, textvariable = value3_, cursor ='left_ptr')
    can.create_window(390,290, window = pseudo3_)


    def hourglass3():
            can['bg']='beige'
            can.delete('all')
            bouton_action = Button(fen, text = 'ACTION', font = 'Helvetica',width = 20, bg = 'red', relief = 'ridge', cursor ='left_ptr', activebackground = 'white', activeforeground = 'red',command = action3)
            can.create_window(250, 175, window = bouton_action)
            bouton_verite = Button(fen, text = 'VERITE', font = 'Helvetica',width = 20, bg = 'red', relief = 'ridge', cursor ='left_ptr', activebackground = 'white', activeforeground = 'red')
            can.create_window(250, 300, window = bouton_verite)

    def action3():
                can.delete('all')
                can['bg']='white'
                w1_ = pseudo1_.get()
                can.create_text(100,50, text = w1_, fill = 'brown', font = 'Century')
                w2_ = pseudo2_.get()
                can.create_text(250,50, text = w2_, fill = 'brown', font = 'Century')
                w3_ = pseudo3_.get()
                can.create_text(400,50, text = w3_, fill = 'brown', font = 'Century')

    bouton_validej3 = Button(fen, relief='raised',bitmap="hourglass", command = hourglass3)
    can.create_window(480,290, window = bouton_validej3)

def joueur4():
    value1__ = StringVar(fen)
    value1__.set("Ton pseudo J1")
    value2__ = StringVar(fen)
    value2__.set("Ton pseudo J2")
    value3__ = StringVar(fen)
    value3__.set("Ton pseudo J3")
    value4__ = StringVar(fen)
    value4__.set("Ton pseudo J4")
    pseudo1__ = Entry(fen, textvariable = value1__, cursor ='left_ptr')
    can.create_window(110,360, window = pseudo1__)
    pseudo2__ = Entry(fen, textvariable = value2__, cursor ='left_ptr')
    can.create_window(250,360, window = pseudo2__)
    pseudo3__ = Entry(fen, textvariable = value3__, cursor ='left_ptr')
    can.create_window(390,360, window = pseudo3__)
    pseudo4__ = Entry(fen, textvariable = value4__, cursor ='left_ptr')
    can.create_window(250,400, window = pseudo4__)


    def hourglass4():
                can['bg']='beige'
                can.delete('all')
                bouton_action = Button(fen, text = 'ACTION', font = 'Helvetica',width = 20, bg = 'red', relief = 'ridge', cursor ='left_ptr', activebackground = 'white', activeforeground = 'red',command = action4)
                can.create_window(250, 175, window = bouton_action)
                bouton_verite = Button(fen, text = 'VERITE', font = 'Helvetica',width = 20, bg = 'red', relief = 'ridge', cursor ='left_ptr', activebackground = 'white', activeforeground = 'red')
                can.create_window(250, 300, window = bouton_verite)

    def action4():
                can.delete('all')
                can['bg']='white'
                w1__ = pseudo1__.get()
                can.create_text(100,50, text = w1__, fill = 'brown', font = 'Century')
                w2__ = pseudo2__.get()
                can.create_text(250,50, text = w2__, fill = 'brown', font = 'Century')
                w3__ = pseudo3__.get()
                can.create_text(400,50, text = w3__, fill = 'brown', font = 'Century')
                w4__ = pseudo4__.get()
                can.create_text(250,70, text = w4__, fill = 'brown', font = 'Century')

    bouton_validej4 = Button(fen, relief='raised',bitmap="hourglass", command = hourglass4)
    can.create_window(400,400, window = bouton_validej4)

def regledujeu():
    can["bg"]="brown"
    can.delete(creation_can2)
    labelrègledujeu = Label(fen, width = 250, height = 250, text = 'Les Règles du jeu \n \n \n Le but est de choisir entre ACTION ou VERITE, ainsi si le joueur choisit ACTION \n il doit réaliser exécuter l\'action et si il choisit VERITE, il doit alors répondre en disant la vérité. \n \n - Si le joueur réussit à répondre ou réussit l\'action il gagne --> 5 points \n \n - Si le joueur remplit l\'action ou répond à la question à moitié il gagne --> 3 points \n \n - Si le joueur ne répond pas à la question ou ne réussit pas l\'action --> 0 point \n \n \n Le premier joueur qui a 25 points remporte le Jeu !!!')
    labelrègledujeu_ = can.create_window(250,250, window = labelrègledujeu)
    bouton_retour = Button(fen, text = "Retour", command = lambda : can.config(can.delete(labelrègledujeu_), bouton_retour.destroy()))
    can.create_window(50,20,window = bouton_retour)




Bouton_Quitter=Button(fen, text ='Quitter', command = fen.destroy)
Bouton_Quitter.pack()


can = Canvas(fen,width = 500, height = 500 , bd=0, bg="brown", cursor ='top_left_arrow', relief = 'raised')
can.create_text(250,25,fill='white',text='NOMBRES DE JOUEURS ?',font = 'ArcadeClassic')
photo = PhotoImage(file ='AOV.gif')
item = can.create_image(250, 250, image =photo)
boutton_play = Button(fen, text ="PLAY", font = 'ArcadeClassic',width = 10, bg = 'beige', relief = 'ridge', cursor ='left_ptr', command = creation_can2 , activebackground = 'black', activeforeground = 'white')
can.create_window(250,480, window= boutton_play)
bouton_regledujeu = Button(fen, text = "Règle du Jeu", command=regledujeu)
bouton_regledujeu_ =can.create_window(50,20, window = bouton_regledujeu)
can.pack(padx=10,pady=10)



fen.mainloop()