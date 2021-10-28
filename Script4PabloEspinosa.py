# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:03:05 2021

@author: Pablo
"""

minu=list("abcdefghij")
mayu=list("KLMNOPQRST")
num=list("0123456789")
esp=list("$%*@")
print ("Introduzca una clave que tenga las siguientes características:\n")
print ("Tamaño mínimo de 5 y máximo de 15 caracteres")
print ("Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j.")
print ("Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T.")
print ("Debe contener al menos un número entre 0 y 9.")
print ("Debe contener un símbolo especial entre: $,%,*,@")
clave=input("Clave: ")
count=0
if len(clave) in range (5,15):
    for i in clave:
        if i in minu:
            count=count+1
    if count!=0:
        count=0
        for i in clave:
            if i in mayu:
                count=count+1
        if count!=0:
            count=0
            for i in clave:
                if i in num:
                    count=count+1
            if count!=0:
                count=0
                for i in clave:
                    if i in esp:
                        count=count+1
                if count!=0:
                    print('Clave aceptada')
                else:
                    print('Clave no válida. Símbolo especial')
            else:
                print('Clave no válida. Números')
        else:
            print('Clave no válida. Mayúsculas')
    else: 
        print('Clave no válida. Minúsculas')
else: 
    print('Clave no válida. Número de caracteres incorrecto')
    
