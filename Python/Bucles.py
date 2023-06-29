edad = 15
num = 0

print("BUCLES INFINITOS <CTRL + C PARA CERRAR>")

'''
while edad < 18:
    print("Eres menor de edad\n")

while True:
    print(num)
    num += 2    

print("Bucles semi-infinitos")

while num <= 100:
    print(num)
    num += 2
print("Primer bucle se terminó <solo porque se escribió el print fuera del while sirve el print>\n")

while num <= 200:
    print(num)
    num +=2
else:
    print("La condición es igual o mayor a 200")
print("El segundo bucle se terminó\n")

while num <= 300:
    print(num)
    num +=2
    if num == 250:           #si se mueve el if a la izq no se escribe la condición        "== es comparar" "= es igual"
        print("La condición es igual a 250")
print("Tercer bucle se terminó\n")
'''
while num <= 400:
    print(num)
    num += 2
    if num == 350:         # error si se salta a la izq pq el break no tiene lógica para if(osea es exclusivo de ciclos, no del if)
        print("Se detiene la ejecución")
        break
print(num)
print("Cuarto bucle terminado\n")


#Loop Infinito + Breack <Útil para poder hacer un menú que solo termine con la palabra clave>
'''while True:
    parametro = input("<")
    if parametro == "exit":
        break
    else:
        print(parametro)
'''

print("02  FOR  ")
print("impresion de una lista de 10 elementos ")
print("\n>>> FOR N°1<<<")

#No está bien optimizado
for i in (1,2,3,4,5,6,7,8,9,10):
    print(i)

print("\n>>> For N°2 <<<")
newlista = [1,2,3,4,5,6,7,8,9,10]
for i in newlista:
    print(i)

print("\n>>> FOR N°3 <<<")
for i in range (10):          #también se puede escribir ->   for i in range (1,11): // <si no se quiere el 0 , no se escribe el 1>
    print(i)

print("\n >>>  FOR N°3 de segunda manera <<<")
for a in range (1,11):
    print(a)
