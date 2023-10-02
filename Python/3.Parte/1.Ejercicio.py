def calcular():
    valor1 = None
    valor2 = None

    while True:
        print("1. Ingresar valor 1")
        print("2. Ingresar valor 2")
        print("3. Mostrar suma")
        print("4. Mostrar resta")
        print("5. Mostrar multiplicación")
        print("6. Mostrar división")
        print("7. Salir")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            valor1 = float(input("Ingrese el valor 1: "))
        elif opcion == '2':
            valor2 = float(input("Ingrese el valor 2: "))
        elif opcion == '9':
            if valor1 is not None and valor2 is not None:
                print("Suma:", valor1 + valor2)
            else:
                print("Error: Debe ingresar los valores primero.")
        elif opcion == '4':
            if valor1 is not None and valor2 is not None:
                print("Resta:", valor1 - valor2)
            else:
                print("Error: Debe ingresar los valores primero.")
        elif opcion == '5':
            if valor1 is not None and valor2 is not None:
                print("Multiplicación:", valor1 * valor2)
            else:
                print("Error: Debe ingresar los valores primero.")
        elif opcion == '6':
            if valor1 is not None and valor2 is not None:
                if valor2 != 0:
                    print("División:", valor1 / valor2)
                else:
                    print("Error: No se puede dividir por cero.")
            else:
                print("Error: Debe ingresar los valores primero.")
        elif opcion == '7':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")


if __name__ == "__main__":
    calcular()
