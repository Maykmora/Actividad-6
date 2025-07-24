def menu():
    print("\n--MENÚ--")
    print("1.Encontrar suma, promedio de n numeros")
    print("2.Calcular el área de un triangulo")
    print("3.Verificar si un numero es par o impar")
    print("4.Calcular el promedio de n calificaciones")
    print("5.Calcular el numero mayor y el menor de n números ")
    print("6.Salir del programa")

def suma_total(lista):
    suma_uno=sum(lista)
    print("\n--SUMA--")
    print(f"La suma de los números es: {suma_uno}")

def promedio(lista):
    prom=sum(lista)/len(lista)
    print("\n--PROMEDIO--")
    print(f"El promedio de los números ingresados es:{prom:.2f}")

def números_positivos(lista):
    positivos = 0
    negativos = 0
    for numero in lista:
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
    print("\n--POSITIVOS Y NEGATIVOS--")
    print("Cantidad de positivos:", positivos)
    print("Cantidad de negativos:", negativos)


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

def mayor_menor(lista):
    mayor=max(lista)
    menor=min(lista)
    print("\n--MAXIMO Y MINIMO--")
    print(f"El maximo de los números ingresados es:{mayor}")
    print(f"El menor de los números ingresados es:{menor}")


while True:
    lista=[]
    lista_dos=[]
    lista_tres=[]
    menu()
    option=input("\nSeleccione una opción del menú: ")

    match option:
        case "1":
            q=int(input("\nIngrese la cantidad de numeros que quiere agregar : "))
            if q>0:
                for i in range(q):
                    p=int(input("Ingrese los numeros de los que desee: "))
                    lista.append(p)
                suma_total(lista)
                promedio(lista)
                números_positivos(lista)
            else:
                print("Error intentelo de nuevo")
        case "2":
            base=float(input("Ingrese la base del triangulo:"))
            altura=float(input("Ingrese la altura del triangulo"))
            print(f"El area del triangulo de {base} x {altura} es {area_triangulo(base,altura)}")

        case "3":
            num=int(input("\nIngrese el numero que desea saber si es par o impar:"))

            num_par_impar(num)

        case "4":
            q=int(input("\nIngrese la cantidad de calificaciones que quiere agregar: "))
            if q>0:
                for i in range(q):
                    p=int(input("Ingrese la calificación que desea agregar:"))
                    lista_dos.append(p)

                promedio_calificaciones(lista_dos)
            else:
                print("Error valor invalido.")

        case "5":
            q = int(input("\nIngrese la cantidad de números que desea comparar: "))
            if q > 0:
                for i in range(q):
                    p=int(input("Ingrese los números que desea comparar:"))
                    lista_tres.append(p)

                mayor_menor(lista_tres)

            else:
                print("Error valor invalido.")

        case "6":
            print("Saliendo del programa")
            break
        case _:
            print("Opción invalida, inténtelo de nuevo")