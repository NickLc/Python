# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 23:31:08 2018
ejercicio1
@author: Nicklc
"""

"""
Escribir una función que reciba como parámetro una cadena de 
palabras separadas por espacios y devuelva, como resultado, 
cuántas palabras de más de cinco letras tiene la
cadena dada.
"""

def contarPalabras(cadena, tam):
    """Cuenta la cantidad de palabras de la cadena que tengan una 
        longitud tam
    """
    palabras = cadena.split()
    cont = 0
    for x in palabras:
        if len(x) == tam:
            cont += 1
    return cont

contarPalabras("estoy utilizando una cadena y una lista", 5)
help(contarPalabras)
