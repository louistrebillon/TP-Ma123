# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:34:29 2021
@author: Asus
"""

from math import exp
import matplotlib.pyplot as p

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
    listen=[]
    listxn=[]
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

print(Newton(X0))

