a = 1
b = 2
print("#### 01 OPERADORES ####")
print("Suma entre a + b es;",a + b)
print("resta entre a - b es:",a - b)


t = 5.39
g = 9.81
v = g * t

print(f"la velocidad del objeto en caida libre es de: {v} m/s")
#print("La velocidad del objeto en caida libre es de {:,2f}".format(v))
print(f"La velocidad del objeto en cailda libre es de :","%.2f" % v)
print("\n")
c1 = 4 + 3j
print(type(c1))

c2 = complex(3, -5)

print ("El numero complejo es:",c2)

print(c2.real)
print(c2.imag)

print("Hola" * 5) #sale 5 veces hola#
# print("Hola" * 3.5 * 2) #no es lógico no sirve
#incompleto# print("Hola" * (int(10 * 2) / 5)), n 

print("###Operadores de comparación ####")
a=1
b=2
print(a == b) # "==" no es lo mismo a "="
print(a != b) # distinto de 
print(a > b)
print(a < b)
print (a <= b)
print (a >= b)

#Operadores de comparación
animal_domestico = "gato"
animal_salvaje = "leopardo"
print(animal_domestico == animal_salvaje)
print(animal_domestico >= animal_salvaje)
print(animal_domestico <= animal_salvaje)
print(animal_domestico < animal_salvaje)
print(animal_domestico > animal_salvaje)
print(animal_domestico != animal_salvaje)
print(len(animal_domestico) == len(animal_salvaje)) #len 

#Operadores logicos
encendido = True
edad = 19
bencina = True

if bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehículo no puede avanzar")

if bencina or encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehículo no puede avanzar")

if not bencina and encendido:
    print("El vehículo puede avanzar")
else:
    print("El vehículo no puede avanzar")

if not bencina or (encendido and edad >= 18):
    print("El vehiculo puede avanzar")
else:
    print("El vehículo no puede avanzar")

if not bencina or (encendido or edad >= 18):
    print("El vehículo puede avanzar")
else:
    print("El vehículo no puede avanzar")