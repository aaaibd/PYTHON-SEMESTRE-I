"reto 01"
nombre = input("¿Cuál es tu nombre?\n")
edad = input("¿Cual es tu edad?\n")
print(type(edad))
total_edad = int(edad) + 20
formato = f"Hola mi nombre es {nombre}, tengo {str(edad)} años y en 20 años tendré {str(total_edad)} años"
print(formato)