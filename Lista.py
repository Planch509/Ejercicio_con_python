import os
os.system('cls')
# declaro la lista
lista = []
# agregamos elementos a la lista
lista.append("Juana")
lista.append("Ana")
lista.append("Walter")
lista.append("Jose")
lista.append("Braulio")

# mostramos la lista
print(lista)
for nombre in lista:
    print(f" {nombre}")

print("---- insertamos un nombre ---")
#inserta un nombre en la ubicación cero
lista.insert(5, "Ximena")
for nombre in lista:
    print(f"* {nombre}")

print("--------Lista ordenada -----")
lista.sort()
for indice in range(len(lista)):
    print(f"* {lista[indice]}")
print("---- Lista al revés ----")
# da vuelta la lista
lista.reverse()
for nombre in lista:
    print(f" {nombre}")

#Eliminación por indice
lista.pop(0)  # elimine el primero
print("--- Eliminamos el primero de la lista ---")
for nombre in lista:
    print(f"* {nombre}")

# Eliminación por el elemento de la lista
lista.remove("Walter")
print("--- Eliminamos por el elemento de la lista ---")
for nombre in lista:
    print(f"* {nombre}")
