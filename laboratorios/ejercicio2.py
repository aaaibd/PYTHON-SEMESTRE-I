#concatenar e imprimir lista
a = [10,9,12,15,18]
b = [21,8,15,3,12]
c = (a+b)
print(c)
print(type(c))
#agregar el numero 30 al final
c = (c) + [30]
print(c)
print(type(c))
#ordenar la lista de forma ascendente
print(sorted(c))
#agregar[4,5,6] al final de la lista ordenada
c = sorted(c) + [4,5,6]
print(c)
print(type(c))
#sumar todos los numeros dentro de la lista
e=sum(c)
print(e)
print(type(e))
#media y mediana de la lista
d = (sorted(c))
f = d[7] - d[6]
f = f /2
d = e / 2
print("El valor de la media es: ",d,"y el valor de la mediana es: ",f)