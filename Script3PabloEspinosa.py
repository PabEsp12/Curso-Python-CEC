# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:04:33 2021

@author: Pablo
"""

Datos = [15, 20, 3,91,4, 5, 6, 7,100,91,110,900,21,33,32, 2, 4,8,10,13,13,16,15,1302]
print(Datos)
print("De estos datos se van a separar los números pares e impares")
pares=[]
impares=[]
for i in range (0,len(Datos)):
    if Datos[i] % 2==0:
        pares.append(Datos[i])
    else:
        impares.append(Datos[i])
print("pares=",pares)
print("impares=",impares)
    