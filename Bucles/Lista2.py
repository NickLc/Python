# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 20:16:06 2018
@Lista 3 de ejercicios
@author: Lazaro Camasca Edson
"""
#Pregunta 1
#Encontrar el maximo y minumo de 4 numeros
numeros = []
for i in range(0,4):
    x = int(input("Ingrese un numero "+str((i+1))+": "))
    numeros.append(x)       # Agregar a la lista
print ("los numeros son: ",numeros,"son del tipo",type(numeros))
#Utilizamos la funcion max() y min() en listas
maximo = max(numeros)
minimo = min(numeros)

print ("El maximo de los numeros es:", maximo)
print ("El minimo de los numeros es:", minimo)

#Pregunta 2
#Determinar si un numero es primo o no
def esPrimo(num):
    cantDivisores = 0
    for i in range(1, num+1):
        residuo = num % i
        if (residuo == 0):
            cantDivisores += 1
        if cantDivisores == 3:
            break
    if cantDivisores == 2:
        return True
    else:
        return False
#-----------------------------------------------------------------
num = int(input("Ingrese un numero positivo: "))

while num < 0:
    num = int(input("Vuelve a ingresar un numero positivo: "))

print ("El numero ",num,"es primo: ",esPrimo(num))


# Pregunta 5
# Ingrese un numero, muestre todos los primos hasta ese numero

def primosHasta(num):    
    primo = []; x = 0
    for i in range(1, num+1):
        if esPrimo(i):
            primo.append(i)
            x +=1
    return primo

num = int(input("Ingrese un numero positivo: "))
print ("Los numeros primos desde ",num,"son:\n",primosHasta(num))
    


    
    
    