# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:34:29 2021

@author: Asus
"""

from math import exp

def f(x) :
    s1= x*exp(x)-7  #Modifier la fonction ici
    return(s1)

def fprim(x) :
    s2= exp(x) + x*exp(x) #Modifier la dérivée de la fonction ici
    return(s2)

def g(x):
    s=x-(f(x)/fprim(x)) 
    return(s)

X0=float(input("Quel est X0 ? "))
epsilon=float(input("Quelle est l'erreur ? "))
Nitermax=float(input("Quel nombre d'itérations max ? "))

def Newton(x) :
    n=0
    xold=X0
    xnew=g(xold)
    erreur=g(xold)-xold

    while abs(erreur)>epsilon and n<Nitermax :
        xnew=g(xold)
        n=n+1
        erreur=xnew-xold
        xold=xnew
    return(xnew)

print(Newton(X0))