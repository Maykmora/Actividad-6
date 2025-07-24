def menu():
    print("\n--MENÚ--")
    print("1.Ingresar n números")
    print("2.Calcular el área de un triangulo")
    print("3.Verificar si un numero es par o impar")
    print("4.Calcular el promedio de n calificaciones")
    print("5.Calcular el numero mayor y el menor de n números ")
    print("6.Salir del programa")


while True:
    menu()
    option=input("\nSeleccione una opción del menú: ")

    match option:
        case "1":
            print("Hola")
        case "2":
            print()

        case "3":
            print()

        case "4":
            print()

        case "5":
            print()

        case "6":
            print("Saliendo del programa")
            break
        case _:
            print("Opción invalida, inténtelo de nuevo")