#---------------------------------------------------------2 EJERCICIO ----------------------------------------------------------------------
#Promedio de temperaturas Durante los 5 días de una semana 
#Se tomaron mediciones de temperatura en la ciudad.
#Se desea conocer cuál fue la temperatura promedio de la semana. Escriba un programa que permita calcularla a partir de
#5 valores de temperatura que ingresará el usuario.
print("--------------------------------------2 Ejercicio -------------------------------------------------")
temperatura1 = float(input("Ingrese la primer temperatura: "))
temperatura2 = float(input("Ingrese la segunda temperatura: "))
temperatura3 = float(input("Ingrese la tercer temperatura: "))
temperatura4 = float(input("Ingrese la cuarta temperatura: "))
temperatura5 = float(input("Ingrese la quinta temperatura: "))

promedio =(temperatura1 + temperatura2 + temperatura3 + temperatura4 + temperatura5)/5
print(f"El promedio de temperaturas de los 5 dias ingresados es: {promedio}")
