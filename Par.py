import os 
os.system('cls')

def generar_numeros_pares(n = 100):
    pares = []
    contador = 0
    numeros = 0
    
    while contador < n:
        if numeros % 2 == 0:
            pares.append(numeros)
            contador +=1 
        numeros += 1
    return pares
    
n= int(input("ingrese la cantidad de numeros pares positivos a generar:"))

if n > 0 :
    pares = generar_numeros_pares(n)
    print(pares)
    print("cantidad de pares :", len(pares))