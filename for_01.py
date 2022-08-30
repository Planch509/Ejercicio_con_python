import os
os.system('cls')
suma = 0
for n in range(1, 8):
    temp = float(input(f"Ingrese temperatura dia {n}:"))
    suma += temp
promedio = suma/7
print(f"Promedio es:{promedio}")
