import os
os.system('cls')
print(" #&#&#& Bienvenido a al casino de Inacap &#&#&# ")
print("¿===desearias un hamburguesa?===")
print("elige su tipo de hamburguesa")
hamburguesa=int(input("1:queso\n2:tocino\n3:doble especial\n4:ninguna \n"))
if hamburguesa<=0 or hamburguesa>=5:
    print("ingrese un valor correcto")
    print("fin del programa")
    exit()
if hamburguesa==1:
    precio=2000 
elif hamburguesa==2:
        precio=2500
elif hamburguesa==3:
        precio=3000
else:
    precio=0
    
print("============================")

print("+++¿Te gustaria añadir una bebida?+++")
print("elige su bebida")
bebida= int(input("1:normal\n2:grande\n3:jugo nectar\n4.ninguna \n"))
if bebida <= 0 or bebida >= 5:
    print("ingrese un valor correcto")
    print("fin del programa")
    exit()
if bebida==1:
    bebida_precio=500
elif bebida==2:
    bebida_precio=1000
elif bebida==3:
    bebida_precio=1000
else :
    bebida_precio=0

print("#######################")
print('"¿Te gustaría selecionar agregados?"')

agregados=int(input("1:papas fritas\n2:empanadas de queso porción 2\n3:empanada de queso porción 4\n4:ninguno\n"))
if agregados <= 0 or agregados >= 5:
    print("ingrese un valor correcto")
    print("fin del programa")
    exit()
if agregados==1:
    ag_precio=600
elif agregados==2:
    ag_precio=500
elif agregados==3:
    ag_precio=900
else:
    ag_precio=0
print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("¿desearias agregar algun postre ?")
postre=int(input("1:vaso helado\n2:fruta a elección\n3:ninguno \n"))
if postre <= 0 or postre >= 4:
    print("ingrese un valor correcto")
    print("fin del programa")
    exit()
if postre==1:
    postre_precio=300
elif postre==2:
    postre_precio=200
else:
    postre_precio=0
print("_________________________________________")

suma = (precio+bebida_precio+ag_precio+postre_precio)
print(suma)
pago=int(input("realizar el pago de sus compras :"))
print("¿que función cumple ud en Inacap?")
print("indiquenos su función")
funcion=int(input("1:estudiante becado\n2:profesor\n3:administrativo\n4:ninguno :"))
if funcion <= 0 or funcion >= 5:
    print("ingrese un valor correcto")
    print("fin del programa")
    exit()
if funcion==1:
    descuento=(suma*0.6)
elif funcion==2:
    descuento=(suma*0.4)
elif funcion==3:
    descuento=suma
else:
    descuento=0

    
total = suma-descuento
print(f"la total de su compra es {total}")
vuelto= total-suma
print(f"su vuelto es: {vuelto}")
print("============================================")
print("Resumen de su compra ")
print(f"la suma total de sus compras : {suma}")
print(f"El descuento que se otrgó debido a su funcion :{funcion} es:{descuento}")
print(f"Su nuevo monto a pagar es de: {total}")
print(f"Su vuelto despues  de su compra es : {vuelto}")
print("Gracias por sus compras")
print("====Fin del Programa===")
