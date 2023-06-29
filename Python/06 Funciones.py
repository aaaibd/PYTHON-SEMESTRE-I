#01 - DECLARANDO FUNCIONES SIMPLES
print("##### DECLARANDO FUNCIONES SIMPLES #####")

def mi_primera_funcion():
    print("Esta es mi primera función")

mi_primera_funcion()  #se escribe el nombre de la funcion + () para que se escriba; def mi_funcion(param1, param2) ---> mi_funcion()

#02 - DECLARANDO UNA FUNCIÓN Y UTILIZANDO LISTAS
print("\n 02 - DECLARANDO UNA FUNCIÓN Y UTILIZANDO LISTAS")

def concatenar(lista1,lista2):
    return lista1 + lista2

lista1 = [1,2,3]
lista2 = [4,5,6]

print(concatenar(lista1,lista2)) #Si solo se escribe concatenar(), no funcionará ya que es necesario llamar a la funcion (lista1,lista2)

#03 - DECLARANDO UNA FUNCIÓN MULTIPLICACIÓN PASANDO PARAMETROS

def multiplicacion (num1,num2):
    return num1 * num2

print(multiplicacion(10,2))


#04 - EJEMPLO DE UNA FUNCIÓN
print("\n#### 04 - FUNCIONES SUMA Y RESTA (POR TECLADO)")

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

a = int(input("ingrese valor de a: "))
b = int(input("ingrese valor de b: "))

resultado = suma(a,b)
print("La suma es de: ",resultado)

resultado2 = resta(a,b)
print("La resta es de: ",resultado2)