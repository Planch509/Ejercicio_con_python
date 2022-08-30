import os
os.system('cls')
lista = []
print("1.enero\n2.febrero\n3.marzo\n4.abril\n5.mayo\n6.junio\n7.julio\n8.agosto\n9.septiembre\n10.octubre\n11.noviembre\n12.diciembre")
mes = int(input("Ingrese mes:"))
while mes<1 or mes>12:
    mes = int(input("Ingrese un número de mes correcto:"))
# separamos los meses que tinenen 31 días
if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
    ejecutar = True
    for i in range(31):
        i+=1
        ejecutar = True
        while ejecutar:
            try:               
                dolar = float(input(f"Ingrese valor dÓlar del día {i}:"))
                lista.append(dolar)                
                ejecutar = False
            except:
                print("Error de ingreso...vuelva a intentar.")
                ejecutar = True
    cantidad_dias=31
# meses con 30 días
elif mes==4 or mes==6 or mes==9 or mes==11: 
    ejecutar = True
    for i in range(30):
        i+=1
        ejecutar = True
        while ejecutar:
            try:               
                dolar = float(input(f"Ingrese valor dolar del día {i}:"))
                lista.append(dolar)                
                ejecutar = False
            except:
                print("Error de ingreso...vuelva a intentar.")
                ejecutar = True
    cantidad_dias=30
# mes de febrero
elif mes==2:
    ejecutar = True
    for i in range(28):
        i+=1
        ejecutar = True
        while ejecutar:
            try:               
                dolar = float(input(f"Ingrese valor dolar del día {i}:"))
                lista.append(dolar)                
                ejecutar = False
            except:
                print("Error de ingreso...vuelva a intentar.")
                ejecutar = True
    cantidad_dias=28
for indice in range(len(lista)):    
    print(f"Valor del dolar en dia {indice+1} es:{lista[indice]}")
# buscamos la mayor y menor alza
mayor = lista[0]
menor = lista[0]
dia_menor = 1
dia_mayor = 2
for i in range(cantidad_dias):
    if lista[i]>mayor:
        mayor = lista[i]
        dia_mayor = i+1
    if lista[i]<menor:
        menor = lista[i]
        dia_menor = i+1
print(f"Mayor alza del dolar fue de:{mayor} el día {dia_mayor}")
print(f"Menor alza del dolar fue de:{menor} el día {dia_menor}")