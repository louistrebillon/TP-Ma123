# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 10:53:43 2021

@author: Asus
"""

from math import exp
import matplotlib.pyplot as p

def f(x) :
    s1=exp(x)-x-10 #modifier la fonction ici
    return(s1)

def secante():
    x0=float(input("Quel est x0 ? "))
    x1=float(input("Quel est x1 ? "))
    err=float(input("Quelle est l'erreur ? "))
    nitermax=float(input("Maximum d'itération ? "))

    
    i=0
    listi=[]
    listxn=[]
    listen=[]
    while i < nitermax and abs(x1-x0) > err :
        listen.append(float(abs(x1-x0)))
        x2= (x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))
        x0=x1
        x1=x2
        i=i+1
        listi.append(float(i))
        listxn.append(x2)
    
    p.figure(figsize=(5,5), dpi=100)
    p.semilogy(listi, listen)
    p.savefig("En=f(n)")
    p.show()
    return (x2,i,listxn,listen)

print(secante())


