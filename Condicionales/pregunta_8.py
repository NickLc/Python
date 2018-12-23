#Preguna 7: Funciones 
import math

def mostrarMenu():
    print("""\n Operaciones:
        1) Suma
        2) Resta
        3) Multiplicacion
        4) Division
        5) Salir
        6) Mostar Operaciones""")


print ("\n\t\t\tCALCULADORA CASERA")    
cont = 1
while(cont):
    print ("""
    1) Ingresar numeros
    2) Salir del Script"""
    )
    opcion1 = int(input("Ingrese una opcion: "))
    if opcion1 == 1:
        numero1 = int(input("Ingrese el primer numero: "))
        numero2 = int(input("Ingrese el segundo numero: "))
        
        mostrarMenu()
        while(cont):
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                print ( numero1, " + ", numero2, "=", numero1 + numero2)
            elif opcion == 2:
                print ( numero1, " - ", numero2, "=", numero1 - numero2)         
            elif opcion == 3:
                print ( numero1, " * ", numero2, "=", numero1 * numero2)
            elif opcion == 4:
                if numero2 != 0:        
                    print (numero1, " / ", numero2, "=", float(numero1 / numero2))
                else:
                    print ("Alerta el numero 2 es: ", numero2)
            elif opcion == 5:
                break
            elif opcion == 6:
                mostrarMenu()
            else :
                print ("Ingrese una opcion valida")

    elif opcion1 == 2:
        break
    
                    
    
