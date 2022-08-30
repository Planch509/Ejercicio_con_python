import os
os.system('cls')

class Persona:
    def __init__(self, Nombre,Apellido,Edad,):
        self.nombre = Nombre
        self.Apellido = Apellido
        self.Edad = Edad
        self.Nota = []

Steeven = Persona("Steeven", "Villefranche", 21)
Gilles = Persona("Francesca", "Gilles",55)

Steeven.Nota =[6.5,6.2,5.5]
Gilles.Nota =[4.4,3.2,5.7]

Alumnos=[Steeven, Gilles]
for e in Alumnos:
    promedio = sum( e.Nota ) / len( e.Nota )

# Olvidé como concatenar. 
#entonces debido a eso no puedo imprimir los alumnos y sus notas.
#Seguiré cuando tengo ganas.     
        
        