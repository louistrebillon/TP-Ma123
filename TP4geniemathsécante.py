# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 10:53:43 2021

@author: Asus
"""

from math import exp

def f(x) :
    s1=x*exp(x)-7 #résultat est 1.52 #modifier la fonction ici
    return(s1)

def secante():
    x0=float(input("Quel est x0 ? "))
    x1=float(input("Quel est x1 ? "))
    err=float(input("Quelle est l'erreur ? "))
    nitermax=float(input("Maximum d'itération ? "))

    i=0
    while i < nitermax and abs(x1-x0) > 0 :
        x2= (x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))
        x0=x1
        x1=x2
        i=i+1
    return (x2)


print(secante())

#Fonctionnent si soit x0 soit x1 est positif et que les deux sont très proches et erreur se choisi pas