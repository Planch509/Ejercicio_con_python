import os
os.system('cls')

class Persona:
    def __init__(self,nombre, edad):
        self.nombre=nombre
        self.edad=edad
        
    def __str__(self) -> str:
        return "Nombre: " + self.nombre + " , edad: " +str(self.edad)
        

class Empleado():
    def __init__(self,nombre,edad,sueldo,cargo):
        super().__init__(nombre,edad)
        self.sueldo=sueldo
        self.cargo=cargo
        
    def __str__(self,sueldo) -> str:
        return super().__str__() + ", Sueldo: " + str(sueldo)
    
        
        
Persona = Persona("Steeven",40)
print(Persona)

empleado = Empleado("Villefranche",22,50000," pentester")
print(empleado)
        
        
    
