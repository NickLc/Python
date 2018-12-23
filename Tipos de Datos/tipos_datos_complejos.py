# Tipos de datos complejos en python
# Tuplas = vector de  constante de diferentes datos simples ( , , , )
# Listas = vector de variables de diferentes datos simples [ , , , ]
# Diccionario = vector de variable con keys elegible

mi_tupla = (4,"hola",3.14,"mundo")
mi_lista = [5,"banano",1.89,"manzano",True]

print ("mi tupla es:", mi_tupla)
print ("mi lista es:", mi_lista)
print ("mi lista del 0 al 2", mi_lista[0:3])   # [0, 3> = [0, 2]
print ("mi lista del 2 al --", mi_lista[2:])
# Nos marcara un error al momento de ejecutar
# mi_tupla[0] = 5

##			AGREGAR ELEMENTO A UNA LISTA

# Podemos agregar elemetos a un lista pero no a una tupla
mi_lista.append("mandarina")
print ("agregando a mi lista:", mi_lista)

# Se puede pasar una tupla a una lista
mi_tupla = list(mi_tupla)

print ("pasado de tupla a lista es:", mi_tupla)
    
mi_tupla[0] = 5
mi_tupla[1] = "HOLA"
mi_tupla[2] = "mundo"

print ("mi lista modificada es:", mi_tupla)

# Se puede pasar una lista a una tupla

mi_tupla = tuple(mi_tupla)

print ("pasado de lista a tupla", mi_tupla)


# Diccionarios
#diccionario = {"clave_1": valor_1, "clave_2": valor_2, ...., "clave_n": valor_n}
#clave_i puede ser un numero, cadena, caracter, etc

mi_diccionario = {2.147: 10, "dos": 2}
print ("Mi diccionario es", mi_diccionario)

## Imprimir el segundo elemento
mi_diccionario["dos"]
# Se puede modificar los valores del diccionario
mi_diccionario[2.147] = "Se cambio a una cadena"
print ("Mi diccionario es", mi_diccionario)

