import os
os.system('cls')
lista = []
ejecutar = True
while ejecutar:
    nombre = input("Ingrese nombre :")
    lista.append(nombre)
    respuesta = input("¿Desea ingresar otro nombre si o no?").lower()
    while respuesta!="no" and respuesta!="si":
        respuesta = input("Respuesta incorrecta ¿Desea ingresar otro nombre si o no?").lower()
    if respuesta=="no":
        ejecutar = False
    else:
        ejecutar = True
os.system('cls')
lista.sort()
for nombre in lista:
    print(f"* {nombre}")

# proceso de busqueda nombre más corto para eliminar
nombre_menos_caracteres = lista[0]
for indice in range(len(lista)):
    if len(lista[indice])<len(nombre_menos_caracteres):
        nombre_menos_caracteres = lista[indice]
# remove borra por el valor     
lista.remove(nombre_menos_caracteres)

print("--- Lista con un nombre menos ---")
for nombre in lista:
    print(f"* {nombre}")
    


