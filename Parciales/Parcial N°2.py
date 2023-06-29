'''
1. Construir un algoritmo que permita generar enteros de 3 en 3 comenzado por el 2 hasta el
valor máximo que será menor que 30. Calcular la suma de los enteros generados que sean
divisibles por 5, y la suma de los enteros generados que sean impares.
'''
#conseguir los numeros (comenzando desde el 2) que se sumen de 3 en 3 hasta el 30
for entero in range(2,30,3):
    entero= entero+entero+1
#Sumar los numeros

#Si la suma de los elementos generados es divisible por 5
if entero % 5 == 0:
    print(entero,"es divisible por 5")
else:
    print(entero,"No es divisible por 5")
#Si la suma de los enteros generados es impar
if not entero% 2 == 0:
    print("El entero es impar")
else:
    print("El entero es par")


'''
2. Calcular la media de calificaciones de la asignatura de Programación. Deducir cuántas son
más altas que la media y cuántas más bajas que dicha media. Se solicita un mínimo de 10
notas. Estas calificaciones se ingresarán por teclado y no se permite notas inferiores a 1,0 ni
mayores a 7,0.
'''


#Ingresar las notas con input (10 notas)
'''notas = input("Ingrese sus notas")
while notas < 10:
    n1 = notas+notas

for Notas in range():
    print(notas)
#Decidir cuales son mayores o menores que la media


#Imprimir notas (no han de ser menores a 1.0 o mayores a 7.0)

'''

'''
Se cuenta con dos sets, los cuales contienen precios de productos:
Set 1 = {100, 250, 300, 1000}
Set 2 = {150, 250, 500, 1000}
A) Verificar si el valor 100 está en ambos sets
B) Comprobar si al menos el valor 500 o 700 está en alguno de los sets
C) Elevar a 3 todos los valores dentro de los sets
D) Unir ambos sets en uno solo
'''
set1 = [100, 250, 300, 1000]
set2 = [150, 250, 500, 1000]

print(type(set1))
print(type(set2))

if set1.count(100) is 1:
    print("Si se encuentra el valor 100 en el primer set")
else:
    print("El valor no se encuentra en el primer set")

if set2.count(100) is 1:
    print("Si se encuentra el valor 100 en el segundo set")
else:
    print("El valor no se encuentra en el segundo set")


if set1.count(500) is 1:
    print("Si se encuentra el valor 500 en el primer set")
else:
    print("El valor no se encuentra en el primer set")
if set1.count(700) is 1:
    print("Si se encuentra el valor 700 en el primer set")
else:
    print("El valor no se encuentra en el primer set")

if set2.count(500) is 1:
    print("Si se encuentra el valor 500 en el segundo set")
else:
    print("El valor no se encuentra en el segundo set")
if set2.count(700) is 1:
    print("Si se encuentra el valor 700 en el segundo set")
else:
    print("El valor no se encuentra en el segundo set")

#sumar ambos sets en una
set3 = set1+set2
print(set(set3))
print(type(set(set3)))