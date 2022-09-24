#!/usr/bin/python3
import sys
import string
import math
''' questa è un'area di commento che uso per indicare cosa fa il programma o sorgente o script.
    Il programma principale o il main, calcola l'area di un triangolo qualsiasi noti i suoi tre
    lati usando la formula di Erone.
    Formula  sqrt p*(p-a)*(p-b)*(p-c)    sqrt = radice quadrata, p = (a+b+c)/2   a,b,c lati
    Salvatelo sul disco con il nome che vi propongo AreaTriangolo.py o come più vi piace
'''
a = int(input('inserisci il primo lato  '))
print('primo lato = ', a)
b = int(input('inserisci il secondo lato  '))
print('secondo lato = ', b)
c = int(input('inserisci il terzo lato  '))
print('terzo lato = ',c)
print("\n");
print(" ora calcolo l'area di questo triangolo")
print("\n")
p = ((a+b+c))/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))

print("l'area  del triangolo è " , s)
