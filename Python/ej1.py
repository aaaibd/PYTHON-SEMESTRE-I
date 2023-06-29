#contar la cantidad de veces que se menciona la palabra "universidad"

texto = ("La Universidad de los Lagos es una institución estatal fundada en 1993. Esta universidad regional  entrega una contribución significativa al desarrollo sostenible del territorio. Como Universidad sus  pilares fundamentales se basan en la inclusión, pluralismo, conciencia ambiental y participación democrática.")
dic =(texto.count("universidad"),)
print("La palabra 'universidad' se repite:",texto.count("universidad"))
print(type(texto),type(dic))


'''
Construir un programa permita calcular e imprimir el resultado de la siguiente sumatoria:
S = 500 + 456 + 510 + 454 + 520 + 452 + ... + 800
'''

'''
Tres empleados de una fabrica trabajan en dos turnos: diurno y nocturno (10 hrs cada 
uno). Se busca calcular el pago diario y el total semanal de cada empleado de acuerdo
con los siguientes puntos:
a) La tarifa del turno diurno por hora es de 12000 CLP.
b) La tarifa del turno nocturno por hora es de 16000 CLP.
c) Los domingos la tarifa se incrementa en 2000 CLP el turno diurno y 3000 CLP el
turno nocturno Ademas considerar:
a) El primer empleado trabaja Lunes, Martes y Miercoles en turnos nocturnos, Jueves y Viernes en turnos diurnos.
b) El segundo empleado trabaja Martes, Miercoles y Jueves turnos nocturnos, y tambien el del domingo en turno diurno.
c) El tercer empleado trabaja Miercoles, Jueves y Viernes diurno, S  abado y Domingo en turnos nocturnos.
Guardar la informacion de cada empleado en un diccionario, con el PAGO DIARIO que debe 
recibir cada empleado y el TOTAL SEMANAL
'''


horas = int(10)
Tdiario = int(12000)
Tnocturno = int(16000)
SalOrdD = Tdiario * horas
SalOrdN = Tnocturno* horas
SalOrdDD = SalOrdD * 0.2
SalOrdND = SalOrdN * 0.3

E1 = SalOrdN * 3 + SalOrdD * 2
print ("El salario del primer trabajador es de: ",int(E1))
E2 = SalOrdN * 3 + SalOrdDD
print ("El salario del segundo trabajador es de: ",int(E2))
E3 = SalOrdD * 3+ SalOrdN + SalOrdND
print ("El salario del tercer trabajador es : ",int(E3))

D = {"Sueldo semanal del empleado 1":int(E1),
     "Sueldo turno diurno diario del empleado 1":int(SalOrdD),
     "Sueldo turno nocturno diario del empleado 1":int(SalOrdN),
     "Sueldo turno diurno Domingo del empleado 1":int(SalOrdDD),
     "Sueldo turno nocturno Domingo del empleado 1":int(SalOrdND),
     "Sueldo semanal del empleado 2":int(E2),
     "Sueldo turno diurno diario del empleado 2":int(SalOrdD),
     "Sueldo turno nocturno diario del empleado 2":int(SalOrdN),
     "Sueldo turno diurno Domingo del empleado 2":int(SalOrdDD),
     "Sueldo turno nocturno Domingo del empleado 2":int(SalOrdND),
     "Sueldo semanal del empleado 3":int(E3),
     "Sueldo turno diurno diario del empleado 3":int(SalOrdD),
     "Sueldo turno nocturno diario del empleado 3":int(SalOrdN),
     "Sueldo turno diurno Domingo del empleado 3":int(SalOrdDD),          
     "Sueldo turno nocturno Domingo del empleado 3":int(SalOrdND)
     }
print(D)





'''
Desarrollar un algoritmo que permita devolver la siguiente propiedad descubierta por
Nicomaco de Gerasa: 
Imprimir por pantalla, los primeros n cubos, considerando el valor de n obtenido desde
teclado.'''



'''Crear 20 numeros, que se encuentren en el intervarlo 40 al 350 y los almacene en una ´
lista y luego pida buscar algun numero dentro de los almacenados. Adem ´ as que muestre ´
la cantidad de ocurrencias de ese numero buscado. (Se permite el uso de la Biblioteca
Random)
'''



'''reloj digital que imprima hora minuto segundo, comenzando desde las 00:00:00 hata las 23:59:59 hrs
'''



'''factorial(x) = 
1 si x = 0
x · factorial(x - 1) si x ≥ 1
'''

n = int(input("ingrese un número: "))
factorial = 1

for i in range(1,n+1):
    factorial*=i
if factorial == 0:
    print(1)
print (f"El fatorial de {n} Es: {factorial}")