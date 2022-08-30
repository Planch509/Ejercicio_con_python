import os
import time
os.system('cls')
precio = []
pizza = []
lista_pizza_pagar = []
lista_precio_pagar = []
lista_contador_pizzas = []
ejecutar = True


def pagar(pizza, precio):
    conjunto = set(pizza)
    for index in range(len(conjunto)):
        contador_pizza = lista_pizza.count(lista_pizza[index])
        lista_pizza_pagar.append(pizza[index])
        lista_precio_pagar.append(contador_pizza*precio[index])
        lista_contador_pizzas.append(contador_pizza)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("--- Bienvenido en la pizzeria de INACAP---")

while ejecutar:
    print("------------------------")
    print("Escoja el tipo de pizza")
    print("1.-pizza Tradicional\t\t$12.000 \n2.-pizza Pepperonni\t\t$14.000 \n3.-pizza todas las carnes\t$16.000 \n4.-Pagar \n5.-Anular Pedido \n6.-Salir")
    try:
        opcion = int(input("Ingrese opcion: "))
        if opcion == 1:
            valor_Pizza = int(12000)
            tipo_Pizza = ("Pizza Tradicional")
            pizza.append(tipo_Pizza)
            precio.append(valor_Pizza)
            print("Producto ingresado con exito!")

        elif opcion == 2:
            valor_Pizza = int(14000)
            tipo_Pizza = ("Pizza Pepperonni")
            lista_pizza.append(tipo_Pizza)
            lista_precio.append(valor_Pizza)
            print("Producto ingresado con exito!")

        elif opcion == 3:
            valorPizza = int(16000)
            tipoPizza = ("Pizza todas las carnes")
            lista_pizza.append(tipoPizza)
            lista_precio.append(valorPizza)
            print("Producto ingresado con exito!")

        elif opcion == 5:
            lista_pizza.clear()
            lista_precio.clear()
            print("Productos eliminados...")
            exe = True
            while exe:
                exe_continue = input(
                    "Desea volver a comprar? 's' para si, 'n' para no:  ").lower()
                if exe_continue == 's':
                    exe = False
                elif exe_continue == 'n':
                    exe = False
                    ejecutar = False
                else:
                    print("Ingreso incorrecto, intente nuevamente...")
                    exe = True

        elif opcion == 6:
            lista_pizza.clear()
            lista_precio.clear()
            print("Saliendo del sistema... espere")
            time.sleep(1.5)
            ejecutar = False
            os.system('cls')

        elif opcion == 4:
            suma = sum(lista_precio)
            newTotal = 0
            diurno = input("Es alumno diurno? s/n: \n").lower()
            if diurno == "s":
                dcto = suma*0.12
                newTotal = suma-dcto
                print(f"Como alumno diurno tiene un 12% de descuento...")
            else:
                print("No tiene descuento!")
                newTotal = suma

            print(f"TOTAL A PAGAR: {newTotal}")
            dinero = int(input("INGRESE DINERO ENTREGADO: "))
            vuelto = 0
            if dinero < newTotal:
                print(
                    f"Dinero insuficiente... Faltan ${dinero-newTotal} pesos")
            else:
                vuelta = dinero-newTotal
                print(f"SU VUELTO ES DE : {vuelto}")

            print("\nPizzería")
            print("----------------------------------------------")
            conjunto = set(lista_pizza)
            pagar(lista_pizza, lista_precio)
            for indice in range(len(conjunto)):
                print(
                    f"{lista_contador_pizzas[indice]}\t{lista_pizza_pagar[indice]}\t{lista_precio_pagar[indice]}")
            if diurno == "s":
                print("----------------------------------------------")
                print(f"Subtotal:\t\t\t${suma}")
                print(f"Descuento:\t\t\t-${dcto}")
            print("----------------------------------------------")
            print(f"Total:\t\t\t\t${newTotal}\n")
            print("----------------------------------------------")
            print(f"Pagó con: ${dinero}")
            print(f"Su vuelta es de : ${vuelta}")
            print("----------------------------------------------")
            ejecutar = False

        else:
            print("Opcion incorrecta... espere... ")
            time.sleep(1.5)
            print("Volviendo al sistema...")
            time.sleep(1)
    except:
        print("Incorrecto! intente nuevamente...")
        print("Espere...")
        time.sleep(1.5)

print("FIN DEL COMPRA ! vuelve pronto...\n\n")
