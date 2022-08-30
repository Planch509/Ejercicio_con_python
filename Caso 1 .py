import os
os.system('cls')

lista_nombres = []
respuesta = "s"
while respuesta=="s":
    nombre = input("Ingrese nombre : ")
    lista_nombres.append(nombre)
    respuesta = input("¿Desea ingresar otro nombre s/n?").lower()
#ordena la lista
lista_nombres.sort()
#mostrar la lista
nombre_mas_caracteres = lista_nombres[0]
for nombre in lista_nombres:
    print(f"* {nombre}")
    if len(nombre) > len(nombre_mas_caracteres):
        nombre_mas_caracteres = nombre
print(f"El nombre más largo es:{nombre_mas_caracteres}")

