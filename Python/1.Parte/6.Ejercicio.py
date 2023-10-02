#---------------------------------------------------------6 EJERCICIO ----------------------------------------------------------------------
print("--------------------------------------6 Ejercicio -------------------------------------------------")
#Asado
#Franco está organizando un asado con sus amigos y necesita de tu ayuda. Para estimar cuánta carne necesita comprar, 
#va a suponer que cada invitado come 0.7 Kg de carne. Ayuda a Franco escribiendo un programa que permita al usuario ingresar 
# la cantidad de invitados y el precio de 1Kg. de carne, 
#y muestre cuántos Kg de carne en total debe pedir al carnicero y cuánto dinero necesita para pagar.

invitados = int(input("Ingrese la cantidad de invitados: "))
precio = float(input("Ingrese el precio del kg de carne: "))

kg_carne = invitados * 0.7
total_a_pagar= kg_carne * precio
print(f"Debera comprar {kg_carne}kg de carne, y el total a pagar es: ${total_a_pagar}") 