import os
os.system('cls')
lista_producto = []
lista_precio = []
ejecutar = True
while ejecutar:
    try:
        os.system('cls')
        print("1.Ingresar producto\n2.Listar Productos\n3.Modficar producto\n4.Eliminar un producto\n5.Salir")
        opcion=int(input("Ingrese opción:"))
        if opcion==1:
            print("== Ingreso de producto ==")
            producto = input("Ingrese producto:")
            precio = int(input("Ingrese precio:"))
            lista_producto.append(producto)
            lista_precio.append(precio)
        elif opcion==2:
            print("== Listado de Productos ==")
            suma = 0
            for indice in range(len(lista_producto)):
                suma+=lista_precio[indice]
                print(f"* {lista_producto[indice]}.....{lista_precio[indice]} ")
            print("----------------------")
            print(f"Total es:{suma}")
        elif opcion==3:
            print("== Modificación de Producto ==")
            nombre = input("Ingrese nombre producto:")
            nuevo_precio = int(input("Ingrese nuevo precio:"))
            encontrado = False
            for i in range(len(lista_producto)):
                if lista_producto[i]==nombre:
                    encontrado = True 
                    indice = i
                    break;               
            if encontrado:
                print("Precio modificado con éxito...")
                lista_precio[indice] = nuevo_precio
            else:
                print("No existe un producto con ese nombre...")
        elif opcion==4:
            print("== Eliminación de Producto ==")
            nombre = input("Ingrese nombre producto:")        
            encontrado = False
            for i in range(len(lista_producto)):
                if lista_producto[i]==nombre:
                    encontrado = True 
                    indice = i
                    break;               
            if encontrado:
                print("Producto eliminado con éxito...")
                lista_producto.pop(indice)
                lista_precio.pop(indice)
            else:
                print("No existe un producto con ese nombre para eliminar...")
        elif opcion==5:
            print("Fin del Programa...")
            ejecutar=False
        else:
            print("Opción incorrecta...")
        pausa = input("Presione Enter para continuar...")
    except:
        print("Error:Ingreso incorrecto...")
        pausa = input("Presione Enter para continuar...")

