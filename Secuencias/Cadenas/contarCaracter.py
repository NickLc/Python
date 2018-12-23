# -*- coding: cp1252 -*-
#!/usr/bin/env python

# Contar cuantas letras "caracter" hay en una cadena x


def contarCaracter(cadena, caracter):
    cont = 0
    for i in cadena:
        if i == caracter :
            cont += 1
    return cont

#Contar si en una cadena hay más "A" que "E"
def masAqueE(cadena):
    """La funcion cuenta si hay mas "A" que "E"
        retorna (True, cant) si hay mas A que E
        (False,cant) en caso contrario 
        donde cant es la diferencia de |Cant_A - Cant_E|
    """
    cantA = contarCaracter(cadena, "A")
    cantE = contarCaracter(cadena, "E")
    cant = cantA - cantE
    if cant > 0:
        return (True, cant)
    else:
        return (False, -cant)
        
#Cuantas vocales hay en una cadena
def contarVocales(cadena):
    """contarVocales cuenta las vocales mayusculas y minusculas que hay en una cadena"""
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    cantVocales = 0
    for i in cadena:
        for vocal in vocales:
            if i == vocal:
                cantVocales += 1
    
    return cantVocales
    
def main():
    cadena = input("Ingrese la cadena: ")
    print("Cantidad de A: ", contarCaracter(cadena, "A"))
    print("Cantidad de E: ", contarCaracter(cadena, "E"))
    print("Hay mas A que E:", masAqueE(cadena))
    print("Cantidad de vocales:", contarVocales(cadena))    
main()
