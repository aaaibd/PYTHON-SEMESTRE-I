print("Construir un programa permita calcular e imprimir el resultado de la siguiente sumatoria: S=500+456+510+454+520+452+...800")
S=0
numeroinicial=500
disminucion=-2
numero = (0)
while numeroinicial <= 800:
    S = S + numeroinicial
    numeroinicial = disminucion + numeroinicial
    numero = numeroinicial + numero
    if numeroinicial % 100 == 0:
        disminucion2 : 10
print("La Lista de numeros es: ", numero)
print("La sumatoria es: ", S)

