"""Generar una lista con 10 valores enteros aleatorios entre 1 y 20 (se puede usar randint() del módulo random). 
Luego: 
1.Muestre la lista
2.El usuario debe ingresar un valor un valor. 
El programa debe informar cuántos valores de la lista son mayores a dicho valor, para eso debe utilizar una función. 
La función debe recibir como argumentos la lista y un entero, y debe retornar la cantidad de valores de la lista mayores a dicho entero.
3.Crear una función que calcule el promedio de la lista y utilizarla.
4.Crear una función que encuentre el valor más grande y el más pequeño de la lista y los retorne."""

import random

def lista_aleatoria():
    lista = []
    for i in range (10):
        numero = random.randint(1,20)
        lista.append(numero)
    return lista

def es_mayor(lista,valor_ingresado):
    cont = 0
    for i in lista:
        if (valor_ingresado<i):
            cont = cont + 1
    return cont

def promedio_lista(lista):
    suma_numeros = 0
    for i in lista:
        suma_numeros = suma_numeros + i
    promedio = suma_numeros/10
    return promedio 

def maximo_minimo(lista):
    maximo = minimo = lista[0]
    for valor in lista:
        if valor > maximo:
            maximo = valor
        elif valor < minimo:
            minimo = valor

    return (maximo, minimo)
#----------------------------------2 APARTADO -------------------------------------
lista = lista_aleatoria()
print(lista)

#---------------------------------3 APARTADO --------------------------------------
valor = int(input("Ingerse un numero: "))
cantidad_numeros_mayores = es_mayor(lista,valor)
print(f"En la lista hay {cantidad_numeros_mayores} numeros mayores a {valor}")

#---------------------------------4 APARTADO ---------------------------------------
promedio = promedio_lista(lista)
print(f"El promedio de valores de la lista es: {promedio}")


#---------------------------------5 APARTADO ---------------------------------------
(max,min) = maximo_minimo(lista)
print(f"El valor maximo es: {max} y el minimo: {min}")