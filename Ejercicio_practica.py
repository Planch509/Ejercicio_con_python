import os
os.system('cls')
pizza_dispo = ["Tradicional", "Peperoni", "Todas las carnes"]
pizza_precio = [12000, 14000, 16000]
Eleccion = []
precio_equi = []
pizza_elijidos = []
ejecutar = True
i = ""
opcion = 0
opcion_pizza = 1
respuesta = "no"
while ejecutar:
    try:
        os.system('cls')
        print("------Bienvenido a la Pizzeria de Inacap------")
        print("------------MENU PRINCIPAL DE LA PIZZERIA------------- ")
        print("1.Elegir Pizza\n2.Pagar\n3.Anular pedido\n4.Salir")
        opcion = int(input("Ingrese opcion:"))
        if opcion == 1:
            print("######## Pizzas disponibles ##########")
            print("1.Tradicional $12.000.-\n2.Peperoni $14.000\n3.Totas las carnes $16.000\n4.Salir")
            opcion_pizza = int(input("elije una opcion"))
            if opcion_pizza == 1:
                print("1.Tradicional $12.000.-")
                pizza_elijidos.append("Tradicional")
                precio_equi.append(12000)
                elijidos.append(1)
            elif opcion_pizza == 2:
                print("2.Peperoni $14.000.-")
                lista_pizza_selec.append("Peperoni")
                lista_precio_selec.append(14000)
                seleccionadas.append(2)
            elif opcion_pizza == 3:
                print("3.Todas las carnes $12.000.-")
                lista_pizza_selec.append("Todas las carnes")
                lista_precio_selec.append(16000)
                seleccionadas.append(3)
            else:
                print("Opcion incorrecta...")
                pausa = input("Presione Enter para continuar...")
        elif opcion == 2:
            print("== Pizzeria==")
            suma = 0
            for indice in range(len(pizza_elijidos)):
                suma += precio_equi[indice]
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
                    i = indice+1
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
                    i = indice+1
                    print(
                        f"*{i}.- {lista_pizza_selec[indice]}.....{lista_precio_selec[indice]} ")
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
            print("== Lista pedido==")
            for indice in range(len(lista_pizza_selec)):
                suma += lista_precio_selec[indice]
                i = indice+1
                print(
                    f"*{i}.- {lista_pizza_selec[indice]}.....{lista_precio_selec[indice]} ")
            item = int(input("ingrese numero del item que desea anular "))
            encontrado = False
            for i in range(len(lista_pizza_selec)):
                if lista_pizza_selec[i] == item:
                    encontrado = True
                    indice = i
                    break
            if encontrado:
                print("Item ilimitado con exito...")
                lista_precio.pop(indice)
            else:
                print("No existe un producto con ese nombre...")
        elif opcion == 4:
            print("== Salir del programa ==")
            ejecutar = False
        else:
            print("Opcion incorrecta...")
        pausa = input("Presione Enter para continuar...")
    except:
        print("Error:Ingreso incorrecto...")
        pausa = input("Presione Enter para continuar...")
