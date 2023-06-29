nombre = input("¿Cuál es el nombre del estudiante?\n")
asignatura = input("¿Cuál es el nombre de la asignatura?\n")
notalab1 = float(input("¿Cuál es la nota 1?\n"))
notalab2 = float(input("¿Cuál es la nota 2\n?"))
promedio = float(notalab1*0.3 + notalab2*0.7)
Diccionario = {
    "Nombre":nombre,
    "Asignatura": asignatura,
    "Nota Laboratorio 1": notalab1,
    "Nota Laboratorio 2": notalab2,
    "Nota Final":f"{promedio:.1f}"}
print(Diccionario)
