import os
usuario1 = None
clave1 = None
usuario2 = None
clave2 = None
usuario3 = None
clave3 = None
opcion = 1
while opcion != 3:
    os.system('cls')
    print("** MENÚ PRINCIPAL **")
    print("1.Iniciar sesión\n2.Registrar usuarios\n3.Salir")
    opcion = int(input("Ingrese opción:"))
 ####  Opción 1 ######
    if opcion == 1:
        print("- Iniciar Sesión -")
        os.system('cls')
        print("--- Login de Acceso ---")
        user = input("Ingrese usuario:")
        passwd = input("Ingrese clave:")
        correcto = False
        if user == usuario1 and passwd == clave1:
            correcto = True
        elif user == usuario2 and passwd == clave2:
            correcto = True
        elif user == usuario3 and passwd == clave3:
            correcto = True

            # si correcto es verdadero hacer
        if correcto:
            opcion2 = 1
            while opcion2 != 3:
                print("= Sub Menú =")
                print("1.Realizar una llamada\n2.Enviar correo electrónico\n3.Cerrar sesión")
                opcion2 = int(input("Ingrese opción:"))
                if opcion2 == 1:
                    print("- Realizar llamada -")
                    #Agregar el código
                elif opcion2 == 2:
                    print("- Enviar correo -")
                    #Agregar el código
                elif opcion2 == 3:
                    print("- Sesión cerrada -")
                    #Agregar el código
                else:
                    print("Opción incorrecta...")
        else:
            print("* Usuario o clave incorrecta...")
            pausa = input("Presione Enter para continuar...")
    #### Opción 2 ########
    elif opcion==2:
        print("- Registro de Usuarios -")
        usuario1=input("Ingrese usuario:")
        clave1=input("Ingrese clave:")
        resp = input("¿Desea ingresar otro usuario s/n?").lower()
        if resp=="s":
            usuario2=input("Ingrese segundo usuario:")
            clave2=input("Ingrese clave:")
            resp = input("¿Desea ingresar un tercer usuario s/n?").lower()
            if resp=="s":
                usuario3=input("Ingrese tercer usuario:")
                clave3=input("Ingrese clave:")
    elif opcion==3:
        print("Fin del programa...") 
    else:
        print("Opción incorrecta")
    pausa=input("Presione Enter para continuar...")
    
