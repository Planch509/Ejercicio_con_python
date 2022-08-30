import os
os.system('cls')
intentos=1
while intentos<=3:
    usuario=input("Ingrese usuario:")
    clave = input("Ingrese clave:")
    if usuario=="pedro" and clave=="1234":
        respuesta="s"
        intentos=4
        tecla=input(f"Bienvenido {usuario}... \n presione Enter para continuar")
    elif usuario=="angel" and clave=="a2s4":
        respuesta="s"
        intentos=4
        tecla=input(f"Bienvenido {usuario}... \n presione Enter para continuar")
    else:
        print("Usuario o clave incorrecta...")
        respuesta="n"
        intentos += 1
        if intentos==4:
            print("*Excediste el limite de intentos...")
    #Aquí comienzan los juegos
    while respuesta=="s":
        os.system('cls')
        # Etapa 2
        print("**** Juego n°1 ****")
        print("¿Cuál de los siguientes animales vive en el agua?")
        print(f"1.Perro\n2.Tiburón\n3.Conejo\n4.Cocodrilo")
        opcion = int(input("Ingrese opción:"))
        if opcion==2:
            puntaje = 1.0
        elif opcion==4:
            puntaje = 0.5
        else:
            puntaje = 0 
        suma = 0
        suma = suma + puntaje
        # Etapa 3
        print("**** Juego n°2 ****")
        print("¿Cuál de los siguientes animales tiene el cuello más largo?")
        print(f"1.Perro\n2.Jirafa\n3.Oso hormiguero\n4.Brontosaurio")
        opcion = int(input("Ingrese opción:"))
        if opcion==4:
            puntaje = 3
        elif opcion==2:
            puntaje = 2
        else:
            puntaje = 0 
        suma = suma + puntaje
        print("**** Juego n°3 ****")
        print("¿Cuál ave es la más grande?")
        print(f"1.Paloma\n2.Aguilucho\n3.Cóndor\n4.Aguila Américana")
        opcion = int(input("Ingrese opción:"))
        if opcion==3:
            puntaje = 3
        elif opcion==4:
            puntaje = 2
        else:
            puntaje = 0 
        suma = suma + puntaje
        print("**** Juego n°4 ****")
        print("¿Cuál de los siguientes animales es un mamífero?")
        print(f"1.Pez espada\n2.Orca\n3.León\n4.Tiburón")
        opcion = int(input("Ingrese opción:"))
        if opcion==2:
            puntaje = 3
        elif opcion==3:
            puntaje = 3
        else:
            puntaje = 0 
        suma = suma + puntaje
        nota = (suma*7)/10
        nota2 = format(nota,".1f")
        print("=====================================")
        print(f"Puntaje obtenido es:{suma}")
        print(f"Nota obtenida es:{nota2}")
        if nota==7.0:
            print("¡Felicitaciones obtuviste el máximo Puntaje!  :-) ")
        print("======================================")   
        respuesta=input("Desea jugar otra vez s-n?").lower()  
print("Fin del programa...")