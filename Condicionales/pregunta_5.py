# -*- coding: cp1252 -*-
#Pregunta 5: Determinar si un año es bisiesto o no

anio = int(input("Ingrese un anio despues de 1600: "))

if(anio % 4 == 0):
    print ("El anio es bisiesto.")
else:
    print ("El anio no es bisiesto.")
    
