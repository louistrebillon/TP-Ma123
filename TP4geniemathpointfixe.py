# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:34:29 2021
@author: Asus
"""

from math import log
import matplotlib.pyplot as p

def g(x):
    s=(7-4*log(x))/3 #Modifier la fonction ici
    return(s)

X0=float(input("Quel est X0 ? "))
epsilon=float(input("Quelle est l'erreur ? "))
Nitermax=float(input("Quel nombre d'itérations max ? "))

def pointfixe(x) :
    n=0-1.
    xold=X0
    xnew=g(xold)
    erreur=g(xold)-xold
    listxn=[]
    listen=[]
    listi=[]

    while abs(erreur)>epsilon and n<Nitermax :
        listen.append(abs(erreur))
        xnew=g(xold)
        n=n+1
        erreur=xnew-xold
        xold=xnew
        listxn.append(xold)
        listi.append(float(n))
        
    p.figure(figsize=(5,5), dpi=100)
    p.semilogy(listi, listen)
    p.savefig("En=f(n)")
    p.show()
    return(xnew,n,listxn,listen)

print(pointfixe(X0))
