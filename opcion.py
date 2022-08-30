import os
os.system('cls')

menu= """ 
1.M_numero
2.M_texto
3.M_signo
4.M_numero_usado
"""

okey= True
for okey in range(5):
    print(menu)
    opcion = int(input("elije una opcion :"))
    if opcion is 1:
      print(545)
    elif opcion is 2:
        print("Hola mundo")
    elif opcion is 3:
        print(f" rrrr")
    elif opcion is 4:
        print("Numero Usado")
    else:
        print("numero fuera de rango")
