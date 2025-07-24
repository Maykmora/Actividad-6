def menu():
    print("\n--MENÚ--")
    print("1.Ingresar n números")
    print("2.Calcular el área de un triangulo")
    print("3.Verificar si un numero es par o impar")
    print("4.Calcular el promedio de n calificaciones")
    print("5.Calcular el numero mayor y el menor de n números ")
    print("6.Salir del programa")

def menu_dos():
    print("1.Encontrar la suma total de n numeros")
    print("2.Encontar el promedio de n números")
    print("3.Encontar la cantidad de números positivos y negativos")
    print("4.Salir")

def suma_total(lista):
    suma1=sum(lista)
    return suma1

def area_triangulo(base,altura):
    area=base*altura/2
    return area

def num_par_impar(num):
    if num%2==0:
        print("El numero ingresado es par.")
    else:
        print("El numero ingresado es impar.")

def promedio_calificaciones(lista):
    g=sum(lista)/len(lista)
    print("\n--PROMEDIO--")
    print(f"El promedio de las calificaciones ingresadas es:{g:.2f}")


while True:
    lista=[]
    lista_dos=[]
    menu()
    option=input("\nSeleccione una opción del menú: ")

    match option:
        case "1":
            while True:
                menu_dos()
                option2=input("\nSeleccione una opción del menu: ")
                match option2:
                    case "1":
                        print()
                    case "2":
                        print()
                    case "3":
                        print()
                    case "4":
                        print()

        case "2":
            base=float(input("Ingrese la base del triangulo:"))
            altura=float(input("Ingrese la altura del triangulo"))
            print(f"El area del triangulo de {base} x {altura} es {area_triangulo(base,altura)}")

        case "3":
            num=int(input("\nIngrese el numero que desea saber si es par o impar:"))

            num_par_impar(num)

        case "4":
            q=int(input("\nIngrese la cantidad de calificaciones que quiere agregar: "))
            for i in range(q):
                p=int(input("Ingrese la calificación que desea agregar:"))
                lista_dos.append(p)

            promedio_calificaciones(lista_dos)




        case "5":
            print()

        case "6":
            print("Saliendo del programa")
            break
        case _:
            print("Opción invalida, inténtelo de nuevo")