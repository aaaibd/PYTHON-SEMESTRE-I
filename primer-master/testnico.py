inicio = 500
final = 800
termino_actual = inicio
suma = 0

while termino_actual <= final:
    suma += termino_actual
    print("Número actual:", termino_actual)
    
    if termino_actual % 2 == 0:
        operacion = "sumar"
        valor = 54
    else:
        operacion = "restar"
        valor = 58
    
    print("Operación:", operacion)
    print("Valor:", valor)
    
    if operacion == "sumar":
        termino_actual += valor
    else:
        termino_actual -= valor

print("El resultado de la sumatoria es:", suma)
