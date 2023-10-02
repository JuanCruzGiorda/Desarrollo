#---------------------------------------------------------3 EJERCICIO ----------------------------------------------------------------------
#Bitcoins a Pesos 
#Escriba un programa que permita a una persona conocer a cuántos Pesos Argentinos equivalen hoy los Bitcoins (BTC) 
#que encontró guardados en un disco rígido viejo. El usuario del programa debe ingresar una cantidad en Bitcoins.
print("--------------------------------------3 Ejercicio -------------------------------------------------")
bitcoins = float(input("Ingrese la cantidad de bitcoins: "))
equivalencia = 8200000 * bitcoins
print(f"La equivalencia en pesos argentinos es: ${equivalencia}")