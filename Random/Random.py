# -*- coding: utf-8 -*-
import random
"""
Created on Sat Dec 22 19:18:10 2018
Paquete Random
@author: ADMIN
"""

random.random()         #Random float x, 0.0 <= x < 1.0
help(random.random)

random.uniform(1, 25)   #Random float x, 1.0 <= x < 25.0
help(random.uniform)    

random.randint(5, 15)   #Integer(entero) x, 5<= x < 15
help(random.randint)

sec = ["hola", 16, 34.6, 4+5j]   #Secuencia = cadena, tupla, lista
random.choice(sec)        #Entrega un valor de la secuencia
help(random.choice)
                            
random.shuffle(sec)     #Permuta(intercambia) los valores de una lista
sec                     #La lista no es inmutable

random.sample(sec, 2)   #Escoge 2 elementos random de la secuencia
