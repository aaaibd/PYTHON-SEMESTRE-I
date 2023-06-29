'''
#Ejercicio número 1 (Falta por añadir la funcion para sumar todos los impares, los pares y todos los números):
def numeroaindicar(num01):
    print(num01)

n = (int(input("Ingrese el número límite: ")))
num01 = 0
while num01 <= n:
    if not numeroaindicar(num01):
        num01 += 1

def numbasumar():
    if num01 % 2 == 0:
        print(num01,"es número par")
    else:
        print(num01,"no es par")
numbasumar()






#Ejercicio número 2:
def ingresarnombres():
    nombres = 0
    while nombres < 5:
        nombres = nombres + 1
        ingresarnombres = input("Ingrese los nombres: ")
        nomb.append(ingresarnombres)
        print(nomb)
nomb = []
ingresarnombres()

def contarlista(listnombr):
    letras = 0
    for nombre in listnombr:
        if isinstance(nombre, str):
            letras += len(nombre)
    return letras
totalletras = contarlista(nomb)
print(totalletras)

def impresionresultados():
    print(f"Los nombres ingresados son: {nomb} y la cantidad de letras que la componen en total es de: {totalletras}")
impresionresultados()

#Ejercicio número 3:
def añobisiesto(año):
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

año = 0
while año <= 400:
    if añobisiesto(año) and añobisiesto(0):
        print(año,"Es un año bisiesto")
    else:
        print(año,"No es un año bisiesto")
    año += 1
'''

'''
4.-Disenar un algoritmo que pueda actuar como un cajero, que devuelve y desglosa el vuelto
en billetes y monedas (pesos chilenos). Utilizando funciones en Python.
'''
#la contraseña es 1234
while True:
    parametro = input()
    if parametro == "1234":
        break
    else:
        print(parametro)




'''
5.-Desarrollar un programa que permita al usuario ingresar una serie de numeros enteros 
positivos (N numeros) hasta que ingrese -1 (Solo positivos ignorando los numeros ne- 
gativos). Luego, el programa debe calcular e imprimir en pantalla lo siguiente: el numero 
mayor de los ingresados, la sumatoria total de los numeros, la sumatoria de los numeros 
pares, la sumatoria de los numeros impares y el promedio total. Ademas, se debe impri- 
mir si el numero mayor obtenido es mayor, menor o igual que el promedio calculado. 
Asegurate de resolver este problema utilizando las funciones que consideres adecua- 
das.


def nnegativo(num01):
    print(num01)
n5 = (int(input("Ingrese el número límite: ")))
num05 = 0
while num05 <= n5:
    if not nnegativo(num05):
        num05 += 1
while True:
    parametro = input()
    if parametro == "-1":
        break
    else:
        print(parametro)
#por mejorar
'''