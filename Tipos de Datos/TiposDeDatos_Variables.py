##Tipos de datos
# las variables en python no se declaran

#Enteros
x = -4

#Reales
x = 3.1552

#Complejos
x = 3 + 5j

#Tipos de cadenas
cadena1 = ('comillas simples')
print (cadena1)
cadena2 = ("comilla doble")
print (cadena2)

#La concatenacion de cadenas se realiza con el signo "+"
n = "aprender"
a = "python"
n_a = "me gusta"+" "+n+" "+a 
print(n_a)

#para saber a que tipo pertenece se utiliza la funcion type()

#Tipos booleanos
aT = True
print("El valor de Verdadero:", aT, ", el cual es del tipo:", type(aT),"\n")

aF = False
print("El valor de Falso:", aF, ", el cual es del tipo:", type(aF),"\n")

#Tipos de Conjuntos: pueden contener diferentes tipos de datos

#Tuplas
pla = 'pastelito', 'jamon', 'papa', 'empanadilla', 'mango', 'quesito'
print(pla)

#Listas
b = ['2.36', 'elefante', 1010, 'rojo']
print (b)
v = b[0:3:2]    #Selecciona del intervalo [0,3] sumando 2 a la posicion 
print (v)

#Tipos de tuplas

#ejemplo simple 
tupla = 19432, 23124, 'hola pyhton!'

#ejemplo de tuplas anidadas
otraTupla = tupla, (1, 5, 3, 6, 5)
#operacion de asignacion a multiples variables
x, y, z = tupla

print (tupla)
print (otraTupla)

#ejemplo de tupla para una conexión con una base de datos
print ("\nConectar a la base de datos MySql")
print ("====================================\n")
conexion_bd = "1454.254.07.18", "accesoroot", "1gh6", "users"
print ("conexion tipica: ", conexion_bd)
print (conexion_bd)

conexion_c = conexion_bd, "3457", "19",
print (conexion_c)
print ("\n")
print ("Acceder a la IP de la base de datos:", conexion_c[0][0])
print ("Acceder al usuario de la base de datos:", conexion_c[0][1])
print ("Acceder a la clave de la base de datos:", conexion_c[0][2])
print ("Acceder al nombre de la base de datos:", conexion_c[0][3])
print ("Acceder al puerto: ", conexion_c[1])
print ("Acceder al tiempo de espera de la conexion:", conexion_c[2])


#Tipos de diccionarios
datos_basicos = {
"nombres": "Fran",
"apellidos": "Pardo Garcia",
"numero": "145548",
"fecha de nacimiento": "03-11-1980",
"lugar de nacimiento": "Madrid - España",
"nacionalidad": "Portuguesa",
"estadp_civil": "Casado"}

print ("\nDetalle del diccionario")
print ("=============================\n")
print ("\nClaves del diccionario: ", datos_basicos.keys())
print ("\nValores del diccionario: ", datos_basicos.values())
print ("\nElementos del diccionaio: ", datos_basicos.items())

#Ejemplo practico de los diccionarios
print ("""
Inscripcion del curso
==========================
Datos del participante
----------------------------"""+
"\nCedula de identidad:", datos_basicos['numero']+
"\nNombre completo: "+ datos_basicos["nombres"] +" "+datos_basicos["apellidos"])
        
#Operadores aritmeticos        
#Suma +
g= 5+1 # g=6

#Resta –
g= 5-1 # g=4

#Negacion –
g= -5+1 # g=-4

#Multiplicacion *
g= 5*2 # g=10

#Exponente **
g= 5**2 # g=25
g
#Division /
g= 5/2 # g=2.5

#Division entera //
g= 5//2 # g=2

#Modulo: divide el operando de la izquierda por el operador del lado derecho y devuelve el resto.
g= 7 % 2 # g=1
        






