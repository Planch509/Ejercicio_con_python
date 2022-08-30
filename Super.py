import os
os.system('cls')
respuesta="si"
while respuesta=="si":
    suma=0
    repetir="si"
    while repetir=="si":
        try:
            precio=int(input("Ingrese precio de producto:"))
            suma+=precio
        except:
            print("Ingreso incorrecto...")
        repetir=input("Ingresa otro precio si/no?")
    print(f"Total de la compra es:{suma}")
    respuesta_socio=input("¿Es socio si/no?")
    if respuesta_socio=="si":
        descuento = suma * 0.05
        total = suma - descuento
        print(f"Como socio tiene un 5% descuento\nTotal a pagar:${total}")
    else:
        print("*No tiene descuento")
    respuesta=input("Desea ingresar una nueva caja si/no?")