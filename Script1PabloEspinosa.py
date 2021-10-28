# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 17:35:51 2021

@author: Pablo
"""

print("Empezando a trabajar con Python\n"
       "Realizado por Pablo Espinosa")
print("Consultadon el tipo de valores")
variables=[875,4.89,"Now is better than never.",1.32,5+8j,8.2] 
#Podría hacerse variable por variable, incluso sin definirlas como en el último print. 
#Pero quería probar de esta manera. 
for i in (0,1,2,3):
    print(f"El tipo de dato de {variables[i]} es:\n", type(variables[i]))
for i in (4,5):
    print(f"El valor {variables[i]} corresponde a un valor entero?\n", isinstance(variables[i],int))
#Podría usarse también dos veces el comando print. 
print("El texto: Readability counts. corresponde a un string?\n", isinstance("Readability counts.",str))


