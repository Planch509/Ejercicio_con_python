import os
os.system('cls')
pizza = ["Tradicional", "Peperoni", "Todas las carnes"]
precio = [12000, 14000, 16000]
elijidos = []
precio_selec = []
pizza_selec = []
ejecutar = True
j = ""
opcion = 0
respuesta = "no"
opcion_pizza = 1
while ejecutar:
    try:
        os.system('cls')
        print("------------MENU PRINCIPA---------------")
        print("1.Elegir Pizza\n2.Pagar\n3.Anular pedido\n4.Salir")
        opcion = int(input("Ingrese opcion:"))
        if opcion == 1:
            print("&&&&&&&&&&&&---Lista de pizzas disponibles---&&&&&&&&&&")
            print("1.Tradicional -\n2.Peperonni\n3.Totas las carnes \n4.Salir")
            opcion_pizza = int(input("Seleccione una opcion"))
            if opcion_pizza == 1:
                print(" elijiste una pizza 1.Tradicional por $12.000.-")
                pizza_selec.append("Tradicional")
                precio_selec.append(12000)
                elijidos.append(1)
            elif opcion_pizza == 2:
                print("2.Peperoni $14.000.-")
                pizza_selec.append("Peperoni")
                precio_selec.append(14000)
                elijidos.append(2)
            elif opcion_pizza == 3:
                print("3.Todas las carnes $12.000.-")
                pizza_selec.append("Todas las carnes")
                precio_selec.append(16000)
                elijidos.append(3)
            else:
                print("Opcion incorrecta...")
                pausa = input("Presione Enter para continuar...")
        elif opcion == 2:
            print("==========================")
            suma = 0
            for indice in range(len(pizza_selec)):
                suma += precio_selec[indice]
                i = indice+1
                print(
                    f"*{i}.- {lista_pizza_selec[indice]}.....{lista_precio_selec[indice]} ")
            print("----------------------")
            print(f"Subtotal:{suma}")
            respuesta = input("Posee descuento si o no?").lower()
            if respuesta == "no":
                suma = 0
                for indice in range(len(lista_pizza_selec)):
                    suma += lista_precio_selec[indice]
                    j = indice+1
                    print(
                        f"*{i}.- {lista_pizza_selec[indice]}.....{lista_precio_selec[indice]} ")
                print("----------------------")
                print(f"Subtotal:{suma}")
                print(f"Descuento: 0")
                Total = Subtotal-descuento
                print(f"Total:{Total}")
            elif respuesta == "si":
                suma = 0
                for indice in range(len(lista_pizza_selec)):
                    suma += lista_precio_selec[indice]
                    j = indice+1
                    print(
                        f"*{j}.- {pizza_selec[indice]}.....{precio_selec[indice]} ")
                print("----------------------")
                Subtotal = suma
                print(f"Subtotal:{Subtotal}")
                descuento = suma*12 / 100
                print(f"Descuento:{descuento}")
                print("----------------------")
                Total = Subtotal-descuento
                print(f"Total:{Total}")
            else:
                respuesta = input(
                    "Respuesta incorrecta posee descuento si o no?").lower()
        elif opcion == 3:
            print("== Anular Pedido==")
            print("----------------------")
            print(f"{pizza_selec} ")
            #os.system('clear')
            print("== Lista pedido==")
            suma = 0
            for indice in range(len(lista_pizza_selec)):
                suma += lista_precio_selec[indice]
                j = indice+1
                print(
                    f"*Item {j}.- {lista_pizza_selec[indice]}.....{lista_precio_selec[indice]} ")
            item = int(input("ingrese numero del item que desea anular "))
            if item == 1:
                pizza_selec.pop(0)
            elif item == 2:
                pizza_selec.pop(1)
            elif item == 3:
                pizza_selec.pop(2)
            elif item == 4:
                pizza_selec.pop(3)
            elif item == 5:
                pizza_selec.pop(4)
            elif item == 6:
                pizza_selec.pop(5)
            elif item == 7:
                pizza_selec.pop(6)
            elif item == 8:
                pizza_selec.pop(7)
            elif item == 9:
                pizza_selec.pop(8)
            elif item == 10:
                pizza_selec.pop(9)
            else:
                print(
                    "Opcion incorrecta, solo se pueden eliminar los 10 primeros productos...")
                pausa = input("Presione Enter para continuar...")

            print("----------------------")
            print("se elimino el Item")
            print("----------------------")
            print("== Pedido Actualizado==")
            for indice in range(len(pizza_selec)):
                suma += lista_precio_selec[indice]
                j = indice+1
                print(
                    f"*{j}.- {pizza_selec[indice]}.....{precio_selec[indice]} ")

        elif opcion == 4:
            print("== Salir del programa ==")
            ejecutar = False
        else:
            print("Opcion incorrecta...")
            pausa = input("Presione Enter para continuar...")
    except:
        print("Error:opcíon incorrecto...")
        pausa = input("Presione Enter para continuar...")
