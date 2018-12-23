# -*- coding: cp1252 -*-
#Ejemplo 1: cuadrado de un numero

def cuadrado(num):
    return num*num

#i toma el valor del intervalo [1, 4>

for i in range(1,4):
    print("cuadrado de "+str(i)+" es: "+str(cuadrado(i)))    

    
"""Todas las instrucciones que describen el cuerpo del ciclo
deben tener una sangría mayor que el encabezado del ciclo.
Esta sangría puede ingresarse mediante espacios o tabuladores, pero
es importante que sea la misma para todas las instrucciones del ciclo."""


#Para pedir ayuda desde el interprete usamos la funcion help()
print("Ayuda desde el interprete usando help()")
help("for")
