import os 
os.system('cls')

"""numeros= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20]
for num in numeros:
    if num%2==0:
        print (num)"""
        
lista = []
N = int(input("ingrese la cantidad de elementos en la lista :"))
for x in range(1, N+1):
    while True:
        num = int(input( "ingrese un numero entero " +str(x) + " : "))
        if num >= 10 and num >= 20:
            break
        else:
            print("ingrese numeros del 10 a 20")
    lista.append(num)
print()
print("los numeros ingresados a la lista son:  "+str(lista))
