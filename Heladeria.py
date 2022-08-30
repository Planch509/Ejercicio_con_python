import os
os.system('cls')
contenedor=True
while contenedor:
    print("\n ###Bienvenido a  mi Heladeria### ")
    
    print("1.vaso chico\n2.vaso mediano\n3.vaso grande\n4.ninguno")
    opcion = int(input("elige su sabor :"))
    if opcion==1:
     vaso="vaso chico 1000$ "
     precio=1000
     contenedor=False
    elif opcion==2:
        vaso="vaso mediano 2000$ "
        precio=2000
        contenedor=False
    elif opcion==3:
        vaso="vaso grande 3500$"
        precio=3500
        contenedor=False
    else:
        print("opcion incorrecta") 
suma=0
suma=suma+precio
contenedor=True
while contenedor:
    print("&&& Relleno &&&")
    print("1.frutillas 500$ \n 2.chocolate 600$ \n 3.ninguno")
    relleno=int(input("elige su relleno :"))
    if opcion==1:
        relleno="frutillas 500$"
        precio=500
        contenedor=False
    elif opcion==2:
         relleno="chocolate"
         precio=600
         contenedor=False
    elif opcion==3:
        relleno=""
        precio=0
        contenedor=False
    else:
         print("opcion incoreccta")
suma=suma+precio
correcto = True
while correcto:
    print("\n== Salsas a Elección ==")
    print("1.Salsa Frutilla $200\n2.Salsa Chocolate $200\n3.Salsa Manjar $300\n4.Ninguno")
    opcion = int(input("Ingrese opción:"))
    if opcion == 1:
        salsa = "Salsa frutilla $200"
        precio = 200
        correcto = False
    elif opcion == 2:
        salsa = "salsa chocolate $200"
        precio = 200
        correcto = False
    elif opcion == 3:
        salsa = "salsa manjar $300"
        precio = 300
        correcto = False
    elif opcion == 4:
        salsa = ""
        precio = 0
        correcto = False
    else:
        print("Opción incorrecta...")
suma = suma + precio
print("=====================================================")
print("Detalle de productos:")
print(f"{vaso}\n{relleno}\n{salsa} ")
print(f"Total venta es:${suma}")
print("=====================================================")
dinero = int(input("Ingrese dinero:"))
if dinero >= suma:
    vuelto = dinero - suma
    print(f"Su vuelto es:{vuelto}")
else:
    print("Falta dinero para pagar...")



    

