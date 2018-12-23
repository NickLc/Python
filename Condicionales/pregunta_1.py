#PREGUNTA 1
# -*- coding: utf-8 -*-
#la codificacion sirve para leer caracteres especiales aparte del ASCII

bailar = input("Te gusta bailar(S/N): ")
cantar = input("Te gusta cantar(S/N): ")

if bailar == "S":
	if cantar == "S":
		print("Llevame contigo ")
	elif cantar == "N":
		print("Te voy enseniar a cantar")
	else:
		print("No ingreso bien la segunda pregunta")

elif bailar == "N":
	if cantar == "S":
		print("Te voy enseniar a bailar")
	elif cantar == "N":
		print("Fuera de aca aburrido")
	else:
		print("No ingreso bien la segunda pregunta")
else:
	print("No ingreso bien la primera pregunta")

