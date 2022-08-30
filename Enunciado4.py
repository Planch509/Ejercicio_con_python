def palindromo():
  num1=int(input("ingrese el primer digito"))
  num2=int(input("ingrese el segundo digito"))
  num3=int(input("ingrese el segundo digito"))
  total_num=(f"{num1} {num2} {num3}")
  ###if num1==num2:
   ### print("los digitos que ingresaste son palindromos")###
  ###else:
    ##print("no es palidromo")
import os
os.system("cls")
ejecutar=True
while ejecutar:
    try:
        print("===========================================")
        print("sistema de verifcacíon de palindromos")
        print("ingrese 3 digitos y vamos a decir si es un palindromo")
        if num1==num2:
           print("los digitos que ingresaste son palindromos")
        else:
           print("no es palidromo")
