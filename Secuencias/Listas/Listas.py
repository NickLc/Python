# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 21:58:38 2018
Listas
@author: Nicklc
"""

#Una lista es una Secuencia mutables, se puede reasignar a sus elementos

"""Se crear con []"""
lista_1 = ["python", 2.56, 4, False, 5 + 4j]

"""Longitud de una lista"""
len(lista_1)
help(len)

""" Elementos de una lista """

#para acceder a los elemtos utilizamos la notacón de las cadenas y tuplas
lista_1[0]
lista_1[10]   #Error
#Se puede acceder desde [0, len(lista)-1]  ó  [-len(lista), -1]
lista_1[-5]


""" Segmentos de una lista """
lista_1[1: 4]       #  [1, 4>
lista_1[0:]         # [0, len(lista)>
lista_1[:3]         # [0, 3>
lista_1[:]      #Toda la lista


""" Cómo mutar listas """

#Cambiar una componente
lista_1
lista_1[1] = 7648
lista_1

"""Metodos de agregado"""
#Agregar un valor al final de la lista
lista_1.append(57853)
lista_1

#Insertar un valor en la posicion k, desplazandose el resto de la lista
lista_1.insert(2, "insertar")
lista_1

#Agregar varios elemtos al final de la lista
lista_1.extend([1, 5, "nuevaLista"])
lista_1

"""Metodos de eliminacion"""
#Eliminar por valor
lista_1.remove(7648)  #si el valor no se encuentra se produce un Error
lista_1                 #Si hay repetidos borrar la primera aparición

#Eliminar el ultimo de la lista
lista_1.pop()
lista_1

#Eliminar por su indice
lista_1.pop(2)
lista_1
"""Metodos de búsqueda"""
#Saber si un elemeto esta en la lista
7586 in lista_1         #retorna True si se encuentra

#Averiguar la posicion de un valor
#index(elemto, indice_inicio, indice_final)
lista_1.index("insertar")   #Error si no se encuentra en la lista

#Contar cantidad de apariciones del elemento
lista_1.count(4)

#Interar los elementos de una lista
for x in lista_1:
    print (x)

"""Metodos de orden"""
l = [5, 2, 5, 6, 1, 7]

#Invertir el orden de la lista
l.reverse()
l
#Obtener la lista ordenada a partir de otra
l_new = sorted(l)
l_new

#Ordenar directamente la lista, Ascendentemente
l.sort()
l
#Odenar directamente la lista, Descendentemente
l.sort(reverse = True)
l

"""Conversion de tipos"""
l = tuple(l)
l
l = list(l)
l
