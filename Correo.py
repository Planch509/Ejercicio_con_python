import os 
os.system('cls')
print("por favor crea un correo")
nombre =input("ingrese su nombre :")
apellido_p=input("ingrese apellido paterno :")
apellido_m= input("ingrese su materno :")
letra=nombre[0:1]
Correo=(letra+apellido_p+apellido_m+"@inacapmail.cl").lower()
print(f"su correo es {Correo}")
