# -*- coding: cp1252 -*-
# Cadenas de caracteres

#!/usr/bin/env python

# Operaciones con cadenas

# Sumar cadenas entre si

cadena1 = "Un divertido "
cadena2 = "programa "
cadena3 = "de radio"

print(cadena1 + cadena2 + cadena3)

# Multiplicar una cadena s por un numero k
print (cadena2 * 4)

# Tamaño de un cadena

tam = len(cadena1)
print ("Tamaño de la cadena1 es: "+str(tam)) #str() convierte a cadena

# Recorrer un Cadena
for x in "recorrer la cadena":
    print (x)

# Acceder a una posicion de la cadena
a = "Aprendiendo Python"
print (a)
print ("Imprime a[2]= "+a[2])    #las cadenas empiezan desde 0
    #se puede utilizar signo negativo para contar desde el ultimo
print ("Imprime a[-1]= "+ a[1])  #Ultimo
print ("Imprime a[-2]= "+ a[2])   #el penultimo

        #Los indices estan -len(a) y len(a)-1

# Segmentos de cadenas
print ("Imprime a[0,2]= "+a[0:2])       # imprime a[0, 2>
print ("Imprime a[-4,-2]= "+a[-4: -2])  # imprime a[-4, -2>
print ("Imprime a[:4]= "+a[:4])         # imprime a[0, 4>
print ("Imprime a[4:]= "+a[4:])         # imprime a[4, len(a)>
print ("Imprime a[:]= "+a[:])           # imprime a[0, len(a)>

# Inmutabilidad, no podemos modificar los caracteres de una cadena
a[2] = "H"              # Error

