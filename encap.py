import os
os.system('cls')


class Persona:
    def __init__(self , nombre, ape_paterno,ap_materno):
        self.nombre=nombre
        self._apellido_paterno = ape_paterno
        self._apellido_materno = ap_materno
        
    def metodo_publico(self):
        self._metodo_privado()
    
    def __metodo_privado(self):
        print(self.nombre)
        print(self._apellido_paterno)
        print(self._apellido_materno)

p1= Persona("Ismael", "Louis" ,"Vehuiah")  
p1.metodo_publico()
print(p1._apellido_paterno)    
