import os
os.system('cls')
lista_producto = []
ejecutar = True
while ejecutar:
    producto = input("Ingrese producto:")
    lista_producto.append(producto)
    respuesta = input("¿Desea ingresar otro producto s/n?").lower()
    while respuesta != "s" and respuesta != "n":
        respuesta = input(
            "Respuesta incorrecta.¿Desea ingresar otro producto s/n?").lower()
    if respuesta == "s":
        ejecutar = True
    else:
        ejecutar = False
#Fuera del while
#ordenamos la lista
lista_producto.sort()
for producto in lista_producto:
    print(f"* {producto}")
