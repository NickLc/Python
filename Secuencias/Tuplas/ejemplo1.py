# -*- coding: utf-8 -*-
import random
"""
Created on Sat Dec 22 19:06:03 2018
@author: Nicklc
Ejercicio 1: Cartas con tuplas 
"""

#----------------------------------------------------------------------
def barajear(baraja):
    """
    barajear() 
        recibe una tupla, retorna la tupla cambiando sus posiciones
    """
    baraja = list(baraja)
    random.shuffle(baraja)        #Error al usar en tuplas
    baraja = tuple(baraja)
    return baraja

#----------------------------------------------------------------------
def seleccionarCartas(baraja, cant):
    """
    seleccionarCartas() 
        recibe una baraja y la cantidad a seleccionar aletoriamente
        retorna una tupla de cartas random
    """
    cartas = []                 #usamos listas
    for i in range(cant):          # [0,5>
        tipo = random.choice(baraja)     #escojemos 1 tipo
        carta = random.choice(tipo)       #escojemos 1 carta
        cartas.append(carta)    #agregamos a la lista
    
    cartas
    cartas = tuple(cartas)      #pasamos a una tupla
    return cartas

#----------------------------------------------------------------------
def poker(cartas):
    """
    Poker(cartas) recibe un conjunto de 5 cartas
        retorna un boolean, si forman un poker(4 cartas del mismo número)
    """
    if len(cartas) != 5:
        print ("Error, la función poker() recibe solo 5 cartas")
    else:
        #Las cartas son de la forma [Numero][Tipo]
        cont_1 = 0; cont_2 = 0
        num_1 = cartas[1][0]; num_2 = cartas[2][0]
        for i in range(len(cartas)):
            if num_1 == cartas[i][0]:
                cont_1 += 1
            if num_2 == cartas[i][0]:
                cont_2 += 1
        if (cont_1 == 4 or cont_2 == 4):
            return True
        else:
            return False
              
#Proponer una representación con tuplas para las cartas de la baraja francesa.

t_espada = ("1E","2E","3E","4E","5E", "6E", "7E","8E", "9E", "10E","JE","QE","KE")
t_corazon = ("1C","2C","3C","4C","5C", "6C", "7C", "8C", "9C", "10C","JC","QC","KC")
t_diamante = ("1D","2D","3D","4D","5D", "6D", "7D", "8D", "9D", "10D","JD","QD","KD")
t_trebol = ("1T","2T","3T","4T","5T", "6T", "7T", "8T", "9T", "10T","JT","QT","KT")

barajear(t_espada)

#Creamos la baraja, anidando tuplas
baraja = (t_espada, t_corazon, t_diamante, t_trebol)    #Anidar tuplas
baraja

"""
Escribir una función poker que reciba cinco cartas de la baraja francesa 
e informe (devuelva el valor lógico correspondiente) si esas cartas forman o 
no un poker (es decir que hay 4 cartas con el mismo número).
"""

cartas = seleccionarCartas(baraja, 5)
cartas
poker(cartas)

cartas = ("8E", "5D", "5T", "5C", "5E")
poker(cartas)
