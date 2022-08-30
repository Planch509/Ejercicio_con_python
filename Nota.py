import os
os.system('cls')
respuesta = "s"
while respuesta == "s":
    suma_gral = 0
    cantidad_estudiantes = int(input("Ingrese cantidad de estudiantes:"))
    cantidad_notas = int(input("Ingrese cantidad de notas:"))
    asignatura = input("Ingrese asignatura:")
    for veces in range(1, cantidad_estudiantes+1):
        print(f"** Estudiante N°{veces} **")
        suma = 0
        for veces_notas in range(1, cantidad_notas+1):
            nota = float(input(f"Ingrese nota {veces_notas}:"))
            suma += nota
        promedio = suma / cantidad_notas
        suma_gral += promedio
        prom = format(promedio, ".1f")
        print("--------------------------------------")
        print(f"Promedio es:{prom}")
    promedio_curso = suma_gral / cantidad_estudiantes
    print(f"Promedio general del curso es:{promedio_curso}")
    respuesta = input("Desea volver a ingresar otra asignatura s/n?").lower()
print("Fin del programa...")
