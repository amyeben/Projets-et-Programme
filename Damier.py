#!/usr/bin/env python
# coding: utf-8

from tkinter import*
#N = int(input("Nombre de cases (entre 1 et 10 ? "))
N = 10
#T = int(input("Tailles de cases (entre 10 et 50 ? "))
T = 50
M = 40 # marge

C = ["beige","pink"]
def damier(N,T):
    for i in range(N):
        for j in range(N):
            posit = (2*M+i*T,2*M+j*T,2*M+(i+1)*T,2*M+(j+1)*T)
            can.create_rectangle(posit, fill = C[(i+j)%2])

    for k in range(N):
        can.create_text(2*M+k*T+0.5*T,1.5*M,text = k+1)
        can.create_text(1.5*M,2.5*M+k*T,text=chr(65+k))
    
fen = Tk()

can = Canvas(fen, width=N*T+3*M, height=N*T+3*M)
can.pack()
damier(N,T)

fen.mainloop()