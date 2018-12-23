# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 23:05:24 2018
Listas y cadenas
@author: Nicklc
"""
#A partir de una cadena se puede obtener una lista
#CADENA  ---->    LISTA

#Funcion split
cadena = "  Una    cadena con   espacios  en  python  "
cadena.split()

#elimina todos los espacios, y devuelve sólo las palabras

cad = "#asdas# d# dasdd #  # 35f#"
cad.split("#")
#Devuelve las componentes que se encuentran entre dos #


# LISTA ---> CADENA
#Funcion Join, inversa de la funcion split
#<separdor>.join(<lista de componentes a unir>)
lista = ["formando", "una", "cadena"]

cad1 = " ".join(lista)
cad1
cad2 = ", ".join(lista)
cad2
cad3 = "%".join(lista)          
cad3
