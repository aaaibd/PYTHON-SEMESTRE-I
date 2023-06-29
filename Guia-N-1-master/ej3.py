# Tres empleados de una fabrica trabajan en dos turnos: diurno y nocturno (10 hrs cada ´
#uno). Se busca calcular el pago diario y el total semanal de cada empleado de acuerdo
#con los siguientes puntos:
#a) La tarifa del turno diurno por hora es de 12000 CLP.
#b) La tarifa del turno nocturno por hora es de 16000 CLP.
#c) Los domingos la tarifa se incrementa en 2000 CLP el turno diurno y 3000 CLP el
#turno nocturno.
#Ademas considerar: ´
#a) El primer empleado trabaja Lunes, Martes y Miercoles en turnos nocturnos, Jueves ´
#y Viernes en turnos diurnos.
#b) El segundo empleado trabaja Martes, Miercoles y Jueves turnos nocturnos, y tam- ´
#bien el d ´ ´ıa domingo en turno diurno.
#c) El tercer empleado trabaja Miercoles, Jueves y Viernes diurno, S ´ abado y Domingo ´
#en turnos nocturnos.
#Guardar la informacion de cada empleado en un diccionario, con el pago diario que debe ´
#recibir cada empleado y el total de la semana
#Construir un programa permita calcular e imprimir el resultado de la siguiente sumatoria:
#S = 500 + 456 + 510 + 454 + 520 + 452 + ... + 800


Diurno = 12000
Nocturno = 12000
domingod = Diurno + 2000
domingon = Nocturno + 3000

empleados = {
    "empleado1": ["nocturno", "nocturno", "nocturno", "diurno", "diurno"],
    "empleado2": ["nocturno", "nocturno", "nocturno", "domingo diurno"],
    "empleado3": ["diurno", "diurno", "diurno", "nocturno", "domingo nocturno"]
}

for empleado, turnos in empleados.items():
    pago_diario = 0
    total_semanal = 0
    
    for turno in turnos:
        if turno == "diurno":
            if "domingo" in turnos:
                pago_diario = Diurno + domingod
            else:
                pago_diario = Diurno
        elif turno == "nocturno":
            if "domingo" in turnos:
                pago_diario = Nocturno + domingon
            else:
                pago_diario = Nocturno
        
        total_semanal += pago_diario
    
    empleados[empleado] = {"pago_diario": pago_diario, "total_semanal": total_semanal}

for empleado, info_empleado in empleados.items():
    print(f"Empleado: {empleado}")
    print(f"Pago diario: {info_empleado['pago_diario']} CLP")
    print(f"Total semanal: {info_empleado['total_semanal']} CLP")
    print()
