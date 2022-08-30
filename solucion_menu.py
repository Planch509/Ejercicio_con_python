import os
import time
usuario1 = None
clave1 = None
usuario2 = None
clave2 = None
usuario3 = None
clave3 = None
logeado = False
opcion=1
while opcion!=3:
    os.system('cls')
    print("** MENÚ PRINCIPAL **")
    print("1.Iniciar sesión\n2.Registrar usuarios\n3.Salir")
    opcion=int(input("Ingrese opción:"))
 ####  Opción 1 ######   
    if opcion==1:
        print("- Iniciar Sesión -")        
        os.system('cls')
        print("--- Login de Acceso ---")
        user=input("Ingrese usuario:")
        passwd=input("Ingrese clave:")
        correcto = False
        if user==usuario1 and passwd==clave1:
            correcto = True
        elif user==usuario2 and passwd==clave2:
            correcto = True
        elif user==usuario3 and passwd==clave3:
            correcto = True           
                
            # si correcto es verdadero hacer
        if correcto:
            print(f"Bienvenido {user}...")
            opcion2=1
            while opcion2!=3:
                print("= Sub Menú =")
                print("1.Realizar una llamada\n2.Enviar correo electrónico\n3.Cerrar sesión")
                opcion2=int(input("Ingrese opción:"))
                if opcion2==1:
                    print("- Realizar llamada -")
                    telefono = input("Ingrese teléfono:")
                    while telefono[0]!="9" or len(telefono)!=9:
                        print("Teléfono incorrecto...")
                        telefono = input("Ingrese nuevamente el teléfono:")
                    print("Teléfono correctamente ingresado...")
                elif opcion2==2:
                     print("- Enviar correo -")
                     encontro= True
                     # mientras encontro es verdadero hacer
                     while encontro:
                         correo = input("Ingrese correo:")
                         for caracter in correo:
                             if caracter=="@":
                                 encontro= False
                                 break   #break abando un ciclo (for)
                         if encontro:
                            print("Debe ingresar un correo correcto...")
                     print("Correo correctamente ingresado...")
                     mensaje = input("Ingrese mensaje:")
                     while len(mensaje)==0:
                         mensaje = input("Debe ingresar un mensaje...Ingrese mensaje:")
                     print("Mensaje ingresado...Correo recibido.")
                elif opcion2==3:
                    print("- Sesión cerrada -")
                    usuario1 = None
                    clave1 = None
                    usuario2 = None
                    clave2 = None
                    usuario3 = None
                    clave3 = None
                    logeado = True
                    print("Cerrando Sesión...")
                    time.sleep(2)
                    print("sesión cerrada...")
                else:
                    print("Opción incorrecta...") 
        else:
            #si logeado es verdadero considerando que se cerro la sesión mostrará mensaje de registrar usuarios
            if logeado:
                print("Debe registrar usuarios...No existen sesiones.")
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
        time.sleep(2)
        os.system('cls')
    else:
        print("Opción incorrecta")
    pausa=input("Presione Enter para continuar...")
    
    
