###ESTE ES UN COMENTARIO DE UNA LINEA

''' ESTE
ES UN COMENTARIO MULTILINEA'''

##GUIA RAPIDA: CONOCIENDO LAS VARIABLES EN PYTHON - 10 DE ABRIL 2023

##-DECLARACNDO VARIABLES DE TIPO CADENA DE TEXTO
nombre = "Constanza"
name = "Victor"
variable = "Sujeto-001"
variables = "Sujetos"
PI = 3.14
'''los identificadores son lo azul, las variables.
    print("etc.etc.etc , variableetc")
        la coma es para separar
        '''


##02 - IMPRESION DE UNA VARIABLE
print(name)
print("hola soy", name)

## DECLARANDO UNA VARIABLE DE TIPO NUMÉRICO
edad = 29


##03 - IMPRESIÓN DE TEXTO + VARIABLE
print ("Mi edad es de", edad)

##04 - IMPRIMIENDO 2 VARIABLES EN UNA MISMA LINEA
#print("Hola mi nombre es" + nombre + "y tengo" +edad + "años")
print("Hola mi nombre es", nombre,"y tengo",edad)
print("Hola mi nombre es"+" "+name+" "+"y tengo " + str ( edad )+" años") ###con signo mas
print("Hola mi nombre es", nombre, "y tengo" , edad, "años") ###con comas
print(f"hola mi nombre es {nombre} y tengo {edad}") ###formato de cadenas (la f obligatoria, va en {Llaves}) no es lo mismo que->[Corchetes (Paréntesis)] )

###06 Multiples variables en una sola linea (no recomendable para multiples variables)
ciudad, region, pais, year = "Puerto montt", "Los lagos", "Chile", "2010"
print("Yo naci en la ciudad de", ciudad,", region de", region,pais,year)

##07 Instruccion comando "Imput"
nombre1 = input("¿Cuál es tu nombre?")
edad1 = input("¿Cual es tu edad?")
print("Tu nombre es:" ,nombre1,"y tu edad es", edad1)