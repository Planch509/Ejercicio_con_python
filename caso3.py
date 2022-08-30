import os
os.system('cls')
lista = []
ejecutar = True
while ejecutar:
    nombre = input("Ingrese nombre:")
    lista.append(nombre)
    respuesta = input("¿Desea ingresar otro nombre si o no?").lower()
    while respuesta!="no" and respuesta!="si":
        respuesta = input("Respuesta incorrecta ¿Desea ingresar otro nombre si o no?").lower()
    if respuesta=="no":
        ejecutar = False
    else:
        ejecutar = True
os.system('cls')
for nombre in lista:
    print(f"* {nombre} ")
nombre_buscado = input("Ingrese nombre a buscar:")
encontrado = False
for indice in range(len(lista)):
    if lista[indice]==nombre_buscado:
        encontrado = True
        ubicacion = indice
        break
if encontrado:
    print(f"El nombre {nombre_buscado} fue encontrado en el indice:{ubicacion}")
else:
    print("No se encontro el nombre en la lista...")
print("Fin del programa...")
