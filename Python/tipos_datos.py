print("hola mundo") #comandos de git hub
"git add ."
"git commit -m mensaje"
"git pull origin main"
"git push -u origin main"
#sort() para ordenar
print("hi")

edad = 29
peso = 70.5
estatura = 1.71
complejo = 1 + 4

print('### 01-datos numéricos ###');
print(f'Mi estatura es de {estatura} y mi peso es de {peso}')
#¿? print('Impresión de un número complejo:' int{complejo})

#transformación e un real a entero
print(peso)
print("transformando un valor real a entero:",int(peso))

imc = peso / (estatura**2)
print(type(imc))
print("Mi Imc es de:",imc,"\n") #
print("Mi IMC es de: {:.2f}".format(imc),"\n") #el :.2f significa que quiero solo 2 decimales, el número es la cantidad de decimales

#02 Datos de tipo cadena de carateres
asignatura = 'Programación'
carrera = "Ingeniería Civil en Informatica"
print("#02-strings#")
print("La asignatura de",asignatura,"corresponde a la carrera de",carrera)

#len (sirve para contabilizar los caracteres de un comando string)
print("La cantidad de caracteres de la palabra", asignatura, "es de:", len(asignatura))
print("La cantidad de caracteres de la palabra", carrera, "esde:",len(carrera))

#03 - Valores booleanos
ampolleta = False
interruptor = True

print('###03-booleans###')
print(ampolleta,interruptor)
print("La variable ampolleta es de tipo:",type(interruptor),"\n") #Con type sabemos el tipo

#Podemos tranformar cualquier valor a un Booleano (al igual que un string, int, etc)
print(bool(0)) #FALSO
print(bool("")) #FALSO
print(bool(None)) #FALSO
print(bool("True")) #VERDADERO
print(bool(1)) #VERDADERO
print(bool("\n")) #VERDADERO

print("###04Listas###")

'''[] sirve para inicializar una lista'''

#Declarando 2 listas diferentes
nueva_lista = list()
otra_lista = []
print("Esta es una lista vacía:",nueva_lista)
print("Esta es otra lista vacía",otra_lista)
print(type(otra_lista))

#Declarando tres listas diferentes
estudiantes = ["Matias", "Marco", "Cristobal", "Sebastian", "Marco"]
num = [1,2,3,4,5,6,1]
print(type(num))
lenguaje = ["Python"]

#Lista de datos compuestos
data = ["Osorno", {'UV : nivel bajo', 'Temp ° C : 15'}, (-40.5725, -73.1353)]
listamixta =['Felipe',100,True]


print("Lista de cadena de caracteres:",estudiantes)
print("lista de números:",num)
print("Lista de un elemento", lenguaje)
print("Esta es una lista mixta:",listamixta)
print("esto igual es una lista:",data)
print(len(listamixta)) #Para saber la cantidad de elementos de una lista
print(estudiantes.count("Marco")) #Cantidad de ocurrencias de un elemento #len cuenta elementos de la lista; count ver la cantidad de ocurrencias de un elemento
print(num.count(1))

lenguaje = ["JavaScript"]
print("Nuevo valor del arreglo de un elemento:",lenguaje)

#Acceder a un elemento específico de la lista (Comienza a contar desde el 0)
print(estudiantes[0]) #correcto (1° elemento de la lista)
print(estudiantes[1]) #(2° elemnto de la lista)
#print(estudiantes[5]) #incorrecto pq está fuera de rango índice/index = lo mismo
print("Posicion -2",estudiantes[-2]) #El negativo significa contar desde atrás


print("Suma de listas",estudiantes + num)

print(list("Python"))
print(list(range(0,5)))
print("\n")

lista = ["D", 2,True]
newtupla = tuple()
grupo1 = ("Daniel","Cristobal","Felipe",200,100,"Daniel")
print("########## 05-TUPLAS ##########")
print(type(grupo1))

#Accediendo al primer elemento de la tupla
print(grupo1[0])

#consultando el elemento "Daniel", cuántas veces se repite/encuentra
print("El elemento se repite:",grupo1.count("Daniel"))

#muestra el indice del primer elemento buscado
print("Indice del elemento:"),grupo1.index("Daniel")

#reasignando el primer elemento de la tupla
#grupo1[0] = "Constanza"
#print(grupo1)
#Las tuplas no se pueden modificar, son inmutables

#obtener un trozo de una tupla
grupo2 = ("Pedro",100,"Felipe","Diego",2020,"Alejandra")
print("Trozo de la pupla",grupo2[0:3])

#Se puede modificar una tupla? (Si pero es ineficiente volver una tupla -> lista y lista -> tupla)
grupo1 = list(grupo1)
print("La tupla ahora es de tipo:",type(grupo1),"\n")
print("\n")

#06- SETS (Conjuntos) - Estructura Fija
#Set es una coleccion no ordenada y sin elementos repetidos. los sets son apliamente utilizados en logica#
#st{}; list[]; dc{}; tp(),
# set{} ;lista[] ;diccionario{}
#Formas de inicializar un Set
print("##### 06-SETS #####")
conjunto_vacio = set()
conjunto_vacio1 = {} #Diccionario o set?
print(type(conjunto_vacio))
conjunto_colores = set({"Azul","Rojo","Verde"}) #Utilizando la funcion set
conjunto_animales = {"Gato","Perro","Loro"} #Utilizando llaves

print(type(conjunto_colores)) #Tipo de dato set
print(type(conjunto_animales))#Tipo de dato set
print("El primer set contiene los siguentes colores",conjunto_colores)
print("El segundo set contiene los siguientes animales",conjunto_animales)

#print(conjunto_animales[0]) # Accediendo al primer elemento al set /No es posible consultar elemento ya que los guarda de manera desordenada,tampoco duplicados.
conjunto_colores.add("Celeste")
print("El set de colores lo conforman:",conjunto_colores)

###06 - DIccionarios ####
diccionario1 = dict()
diccionario2 = {}

datos_personales = {
    "Nombre":"Victor",
    "Institución":"Ulagos",
    "Edad":29,                                              #<-----Es un string tmb los de arriba
    "Asignaturas": {"Esctructura de datos","Programación"} #<---es un set
}

print("Diccionario inicial:",datos_personales)

#Consultar cantidad de elementos del diccionario
print(len(datos_personales))

#Para acceder a sus elementos
print(datos_personales["Institución"])

#Actualizar una clave
datos_personales["Institución"] ="USS"
print("Diccionario actualizado:",datos_personales)

#agregar una nueva clave
datos_personales["Ciudad"] = "Osorno"
print(datos_personales)
#Eliminar
del datos_personales["Ciudad"]
