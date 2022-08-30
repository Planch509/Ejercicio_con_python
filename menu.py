import os

opcion = 1

while opcion != 3:

    try:

        os.system('cls')
        print("** Menú **")
        print("1.Suma\n2.Resta\n3.Salir")
        opcion = int(input("Ingrese opción:"))

        while opcion < 1 or opcion > 3:
            print("Ingreso de opción incorrecta...")
            opcion = int(input("Ingrese opción:"))

        if opcion == 1:
            valor1 = int(input("Ingrese número:"))
            valor2 = int(input("Ingrese otro número:"))
            suma = valor1 + valor2
            print(f"Suma es:{suma}")

        elif opcion == 2:
            valor1 = int(input("Ingrese número:"))
            valor2 = int(input("Ingrese otro número:"))
            resta = valor1 - valor2
            print(f"Resta es:{resta}")

        else:
            print("Fin del programa...")
        pausa = input("Presione Enter para continuar...")

    except:
        print("Error:Ingreso incorrecto...")
        pausa = input("Presione Enter para continuar...")
