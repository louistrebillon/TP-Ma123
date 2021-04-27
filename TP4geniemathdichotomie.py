# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:34:29 2021

@author: Asus
"""

from math import exp

def f(x):
    s1=x*exp(x)-7 #Modifier la fonction ici
    return(s1)

def dicho():
    a=float(input("Quel est x0 "))
    b=float(input("Quel est x1 "))
    err=float(input("Quelle est l'erreur? "))
    nitermax=float(input("Maximum d'itération ? "))
    
    listxn=[]
    listen=[]
    i=0
    m=0
    while abs(b-a) > err and i < nitermax:
        listen.append(abs(b-a))
        m=(a+b)/2
        if (f(a) * f(m) <= 0) :
            b = m
            listxn.append(b)
        else :
            a = m
            listxn.append(a)
        i=i+1
    return(a,i,listxn,listen)
    
print(dicho())
