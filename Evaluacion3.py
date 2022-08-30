import os
os.system('cls')
menu_pizza = []
respuesta = "s"
while respuesta == "s":
    print("------Bienvenido en la Pizzeria de inacap-----")
    print("Tipos de pizzas disponible : \n1.:tradicional\n2.:peperonni\n3.:todas las carnes")
    pizza = input("Elije el tipo de pizza de su gusto : ")
    menu_pizza.append(pizza)
    respuesta = input("¿Desea elijir otro pizza s/n?").lower()
