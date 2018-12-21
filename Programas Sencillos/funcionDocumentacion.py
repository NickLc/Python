# -*- coding: cp1252 -*-
#Documentacion de funciones

#!/usr/bin/env python

"""
Cada funcion realiza una tarea especifica, cuando se tiene
muchas funciones es dif�cil saber exactamente que hace.

Por eso importante documentar cada funci�n

La documentaci�n se coloca luego del encabezado de la funci�n
ejemplo:
"""

def hola(nombre):
    """ Imprime en pantalla un saludo, dirigido a la persona que
        indica el parametro"""
    print ("Hola "+nombre+"!")
    print ("Estoy programando en Python.")


"""
Cuando la funcion esta correctamente documentada, es posible
acceder a su documentacion mediante help()
>>> help(hola)
"""


    
