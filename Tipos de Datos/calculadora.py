#Calculadora
import math
import os

print ("\n\tCALCULADORA PYTHON\n")

print ("""	1)Mostar Menu
	2)Operacion
	3)Salir""")

op = 1
while op != 3 :

	op = float(input("Ingrese una Opcion: "))
	
	if op == 1:			
		print ("""Menu de Operaciones:
		1)Suma
		2)Resta
		3)Multiplicacion
		4)Division
		5)Potenciacion
		6)Logaritmo
		""")
	if op == 2:
		opc = float(input("Ingrese la Operacion: "))

		if opc == 1 :
			print ("a + b")
			a = float(input("a = "))
			b = float(input("b = "))
			print (str(a)+" + "+str(b)+" = ",str(a+b))  

		elif opc == 2 :
			print ("a - b")
			a = float(input("a = "))
			b = float(input("b = "))
			print (str(a)+" - ",str(b)," = ",a-b)  

		elif opc == 3 :
			print ("a x b")
			a = float(input("a = "))
			b = float(input("b = "))
			print (str(a)+" x ",str(b)," = ",a*b)  

		elif opc == 4 :
			print ("a / b")
			a = float(input("a = "))
			b = float(input("b = "))
			print (str(a)+" / ",str(b)," = ",a/b)

		elif opc == 5:
			print ("a ^ b")
			a = float(input("a = "))
			b = float(input("b = "))
			c = math.pow(a,b)
			print (str(a)," ^ ",str(b)," = ",c)

		elif opc == 6:
			print( "log (",a,") en base (",b,")")
			a = float(input("a = "))
			b = float(input("b = "))
			c = math.log(a,b)
			print ("log("+str(a)+") en base "+str(b)+" = ",c)


os.system("cls")
print ("Se a cerrado la CALCULADORA PYTHON")