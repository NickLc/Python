#numero entero
a = 14.0
b = 5

#numero real
c = 4.214
d = 2.1

print( "Los numeros numeros enteros son: ",a," y ",b,"\n")
#print( "los numeros reales son :",c," y ",d )

#cadenas

suma = a+b
resta = a-b
por = a*b
div = a/b
mod = a%b

#mensajes
print( a," + ",b," = ",int(suma))
print( a," - ",b," = ",resta)
print( a," * ",b," = ",por)
print( a," / ",b," = ",div)
print( a," % ",b," = ",mod)

if a > b:
	print( a," es mayor que ", b)