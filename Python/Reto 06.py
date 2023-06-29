'''Reto 6
Obtener los números del rango 10 al 30,
incrementando de 2 en 2. A continuación,
sumar todos los números obtenidos.
'''
i= 10
while i <= 30:
    print(i)

    i += 2
    if i == 30:         # error si se salta a la izq pq el break no tiene lógica para if(osea es exclusivo de ciclos, no del if)
        print("Se detiene la ejecución")
        break

'''for i in range(10):'''