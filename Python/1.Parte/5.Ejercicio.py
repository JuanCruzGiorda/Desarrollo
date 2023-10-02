#---------------------------------------------------------5 EJERCICIO ----------------------------------------------------------------------
print("--------------------------------------5 Ejercicio -------------------------------------------------")
#Club deportivo
#Un club deportivo tiene 4 categorías de asociados según la edad:
#infantiles (desde 13 a 15 años)
#cadetes (a partir de los 15 y hasta 17)
#juveniles (desde los 17 hasta los 19)
#mayores (de 19 años en adelante)
#Escriba un programa que permita al usuario ingresar el nombre y la edad de un socio y muestre el nombre de la categoría en la que 
#le corresponde estar.

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if(edad<13):
    print(f"Hola {nombre}, no hay categoria disponible para su edad")
    
elif(edad >= 13 and edad < 15):
    print(f"Hola {nombre}, su categoria es: infantiles")

elif(edad>= 15 and edad < 17):
    print(f"Hola {nombre}, su categoria es: cadetes")

elif(edad>=17 and edad < 19):
    print(f"Hola {nombre}, su categoria es: juveniles")

else:
    print(f"Hola {nombre}, su categoria es: mayores")