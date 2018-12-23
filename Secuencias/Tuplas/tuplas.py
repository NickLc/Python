# -*- coding: cp1252 -*-
# Tuplas

#!/usr/bin/env python


"""
Las tuplas son un tipo de dato complejo, puede contener numeros,
cadenas, booleanos, etc
"""
#Las tuplas se asignan entre parentesis
t = (25, "Junio", 123.45, True)

"""Longitud de una tupla"""
len(t)

"""Elementos"""
t[0]     # 25
t[1]     # Junio
t[5]     # Error

"""Notacion de rangos"""

t[:2]    # 25, Junio   [0,2>
t[1:]    # Junio, 123.45, True   [0,len(t)>

"""Inmutabilidad, no se puede cambiar los elementos"""
t[0] = 45    #Error

#Para cambiar pasar a una lista, luego a una tupla
l = list(t)     #Pasar a una lista
l[0] = 45
t = tuple(l)    #Pasar a una tupla
t

"""Tupla unitaria, colocar una coma"""

t_uni = ("unitario",)
len(t_uni)

"""Empaquetado y desempaquetado de tuplas"""
#Empaquetado: Asignacion de una secuencia separado por comas 
a = 125
b = "hOLA"
c = 12 + 4j
t_emp = a, b, c
t_emp
#Desempaquetado
x, y, z = t_emp
x
y
z

"""Recorrer una tupla"""
for i in t_emp:
    print (i)
    
