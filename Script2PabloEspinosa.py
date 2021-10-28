# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 18:42:37 2021

@author: Pablo
"""

print("Programa que identifica el tipo de dato de un valor ingresado por el usuario, se realizarán cinco interacciones:")
iteraciones=["Primera","Segunda","Tercera","Cuarta","Quinta"]
for i in (0,1,2,3,4):
    dato=input(f"{iteraciones[i]} Interacción, ingrese un valor cualquiera:"  )
    print("El tipo de dato en Python es:")
    print(type(dato))
print("\n¡YA NO SE HARÁN MÁS INTERACCIONES!")

