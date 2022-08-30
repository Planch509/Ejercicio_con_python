import os
os.system('cls')
dia= int(input("ingrese el dia :"))
if dia>=1 and dia<=7:
 if dia==1:
  print("hoy es lunes")
 if dia==2:
   print("hoy es martes")
 if dia==3:
   print("hoy es miercoles")
 if dia==4:
   print("hoy es jueves")
 if dia==5:
   print("hoy es viernes")  
 if dia==6:
   print("hoy es sabado") 
 elif dia==7:
   print("hoy es domingo") 
else:
   print("no existe ese dia")
print("fin del programa")

