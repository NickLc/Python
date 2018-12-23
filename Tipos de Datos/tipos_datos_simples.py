#Tipos de datos en python
#Se puede pasar de un tipo a otro sin ningun problema
#cadenas
cadd = "cadena doble comilla"
cads = "cadena simple comilla"
cadm = """cadena multilineal
cadena1
cadena2
.
.
.
cadena n\n"""

#numero entero
ne = 10


#numero entero hexadecimal
neh = 0x23

#numero real
nr = 2.155


#Boolean(verdadero/falso)
v = True
f = False

print ("Los tipos de datos simples en python son:\nCADENAS:\n")
print (cadd)
print (cads)
print (cadm)
print ("numero entero: ",ne)
print ("numero entero hexadecimal",neh)
print ("numero real",nr)
print ("Boolean",v)
print ("Boolean",f)

nr = 2
print (nr)
nr = "se paso a una cadena"
print (nr)