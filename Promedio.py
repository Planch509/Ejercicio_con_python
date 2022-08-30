import os
os.system('cls')
nota1=float(input("ingresa nota1 : "))
nota2=float(input("ingresa nota2 : "))
nota3=float(input("ingresa nota3 : "))

promedio=(nota1+nota2+nota3)/3
print(f"promedio es: {promedio}")
if promedio>=4:
    print("Alumno aprobado")
    print("Se paso de curso")
else :
    print("Alumno reprobado") 
       
