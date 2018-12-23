# -*- coding: cp1252 -*-
#Construir programas y modulos

#!/usr/bin/env python

#Esta linea es para que se pueda ejecutar
#en SO Unix, python es multiplataforma


"""Un programa sencillo, para calcular cuadrados de numeros"""


def main ():
    print ("Se calcularán cuadrados de números")


    n1 = int(input("Ingrese un número entero: "))

    n2 = int(input("Ingrese otro número entero mayor que anterior: "))

    for x in range(n1, n2):
        print ("Cuadrado("+str(x)+") = "+ str(x*x))

    print ("Es todo por ahora")

main()


"""Para ejecutar el codigo en la linea de comandos colocar
>>>import nombreArchivo

La palabra import le indica a Python a traer a la memoria el modulo
nombreArchivo.py, y ejecutarlo

- Se carga en memoria la funcion main()
- se inicia inmediatamente, la funcion main()

Una vez importado el modulo, este se queda en memoria y puede
volverse a invocar sin necesidad de importarlo nuevamente

>>>cuadrado.main()

"""

