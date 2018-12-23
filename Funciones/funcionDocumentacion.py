# -*- coding: cp1252 -*-
#Documentacion de funciones

#!/usr/bin/env python

"""
Cada funcion realiza una tarea especifica, cuando se tiene
muchas funciones es difícil saber exactamente que hace.

Por eso importante documentar cada función

La documentación se coloca luego del encabezado de la función
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


    
