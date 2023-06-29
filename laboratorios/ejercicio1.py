diccionario = {
    "Región 8":"Bio Bio",
    "Región 10":"Los lagos",
    "Superficie 1":"23890",
    "Superficie 2 ":"48583",
    "Habitantes 1":"1556805",
    "Habitantes 2":"828708"}
#Guardar la información de la tabla en un diccionario, luego imprimir el diccionario por consola
print(diccionario)

#crear clave densidad, densidad = habitantes/superficie
d1 = 1556805 / 1556805
d2 = 828708/ 48583

diccionario["Densidad 1"] = f"{d1:.1f}"
diccionario["Densidad 2"] = f"{d2:.1f}"

#agregar clave capital
diccionario["Capital 1"] = "Concepción"
diccionario["Capital 2"] = "Puerto Montt"

#agregar clave comunas
diccionario["Comunas Bio Bio"] = " Lota, Lebu, Los Ángeles"
diccionario["Comunas Los lagos"] = " Castro, Puerto Varas, Purranque"
#agregar clave provincia en tuplas
provincia1 = ("Biobío", "Arauco", "Concepción""\n")
provincia2 = ("Osorno", "Llanquihue", "Chiloé","Palena""\n")
print(type(provincia1))
print(type(provincia2))
diccionario["Provincia 1"] = provincia1
diccionario["Provincia 2"] = provincia2

#imprimir diccionario versión final
print(diccionario)