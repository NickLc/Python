
#Condicionales en python
#los condicionales son if, elif, else
#problema de calcular el menor y mayor numero de un vector

a = int(input("Ingresa en primer numero:"))
b = int(input("Ingresa en segundo numero:"))
c = int(input("Ingresa en tercer numero: "))

mayor = a
med = b 
menor = c

#algoritmo para encontrar su posicion

if b > a:
	if b > c:
		mayor = b
		if a > c:
			med = a
			menor = c

		else:
			menor = a
			med = c
	else:
		mayor = c
		med = b
		menor = a

else:
	if a > c:
		mayor = a
		if b > c:
			med = b
			menor = c

		else:
			menor = b
			med = c
	else:
		mayor = c
		med = a
		menor = b

print("el mayor es: ",mayor)
print("el medio es: ",med)
print("el menor es: ",menor)