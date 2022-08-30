import os 
os.system('cls')
cadena= input(" ingrese un texto :")
#len (length) cuenta la cantidad de caracteres de una cadena
largo= len(cadena)
print(f"{cadena} tiene {largo} caracter")
#Buscar una palabra y retornar en el endice 
indice = cadena.find ("franche")
print(f" ven se encuentra en el {indice}")
#upper convierte en mayuscula
mayuscula = cadena.upper()
print(f"en mayuscula es {mayuscula}")
#lower convierte en minuscula
minuscula =cadena.lower()
print(f"en minuscula  es {minuscula}")
#contar desde el indice hasta la cantidad de caracter
subcadena = cadena [0:3]
print(f"subcadena hasta {subcadena}")
subcadena=cadena [3:7]
print(f"subcadena de .. hasta {subcadena}")
txt = "The best steeven in life are free!"
if "steeven" in txt:
    print("Yes, 'steeven' is present.")
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"
