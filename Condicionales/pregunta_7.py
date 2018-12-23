#Preguna 7: Funciones Trigonometricas
import math
def mostrarMenu():
    print("""\nFunciones:
        1) Sin(x)
        2) Cos(x)
        3) Tan(x)
        4) Salir
        5) Mostar Funciones""")


print ("\n\t\t\tFunciones Triginometricas")
cont = 1
while(cont):
    print ("""
    1) Ingresar un numero
    2) Salir del Script
    """)
    
    opcion1 = int(input("Ingrese una opcion: "))
    if opcion1 == 1:
        numero = int(input("Ingrese el numero: "))
        mostrarMenu()
        while(cont):
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                print ("sin(", numero, ") = ", math.sin(numero))
            elif opcion == 2:
                print ("cos(", numero, ") = ", math.cos(numero))      
            elif opcion == 3:
                print ("tan(", numero, ") = ", math.tan(numero))
            elif opcion == 4:
                break
            elif opcion == 5:
                mostrarMenu()
            else :
                print ("Ingrese una opcion valida")

    elif opcion1 == 2:
        break
    
                    
    
