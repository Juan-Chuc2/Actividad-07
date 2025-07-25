def saludar():
    print("Bienvenido al Programa de operaciones matematicas")
def suma_total(numbers):
    return sum(numbers)
def calcular_promedio (numbers):
    return sum(numbers)/len(numbers ) if numbers else 0
def contar_positivos_negativos_y_ceros(numbers):
    positivos = 0
    negativos = 0
    ceros = 0
    for number in numbers:
        if number > 0:
            positivos += 1
        elif number < 0:
            negativos += 1
        else:
            ceros +=1
    return positivos, negativos, ceros
def obtener_multiplos_de_3(numbers):
    multiplos =[]
    for number in numbers:
        if number %3==0:
            multiplos.append(number)
    return multiplos
def calcular_area_de_un_rectangulo(base, altura):
    return  base*altura
def calcular_el_perimetro_de_un_rectangulo(base, altura):
    perimetro = (2*base) + (2*altura)
    return perimetro
def es_primo(n):
    if n < 2 or n != int(n):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
saludar()
while True:
    print("\n ===MENU===")
    print("1. Ingreso de lista de n numeros y mostrar")
    print("2. Calcular el area y perimetro de un rectangulo")
    print("3 Verificar si un numero ingresado es primo o no ")
    print("4. Calcular el promedio de n calificaciones y clacificar")
    print("5. Ingresar una lista de n numeros y mostrar")
    print("6. Calculadora de operaciones basicas")
    print("7. Salir")
    option = input("Que operacion desea realizar (1-7) ")
    match option:
        case "1":
            print("\n --Lista de numeros--")
            number_user = int(input("Cuantos numeros desea ingresar "))
            numbers = []
            for i in range(number_user):
                number = float(input("Ingrese los numneros "))
                numbers.append(number)
            positivos, negativos, ceros = contar_positivos_negativos_y_ceros(numbers)
            print("\n --Resultados--")
            print(f"La suma total es: {suma_total(numbers)}")
            print(f"El promedio de los numeros es: {calcular_promedio(numbers)}")
            print(f"la cantidad de numeros negativos son: {negativos}")
            print(f"la cantidad de numeros positivos son: {positivos}")
            print(f"la cantidad de numros ceros son: {ceros}")
            print(f"los multiplos de 3 son: {obtener_multiplos_de_3(numbers)} ")
        case "2":
            print("\n --Calcular area y perimetro de un rectangulo")
            base = float(input("Ingrese la medida de la base del rectangulo "))
            altura = float(input("Ingrese la medida de la altura del rectangulo "))
            print(f"El area de el rectangulo es: {calcular_area_de_un_rectangulo(base, altura)}")
            print(f"El perimetro del rectangulo es: {calcular_el_perimetro_de_un_rectangulo(base, altura)}")
        case "3":
            numero = input("Ingrese un número para verificar si es primo: ")

            if numero.replace('.', '', 1).replace('-', '', 1).isdigit():
                numero = float(numero)
                if es_primo(numero):
                    print(int(numero), "es un número primo.")
                else:
                    print(int(numero), "NO es un número primo.")
            else:
                print("Entrada inválida. Debe ingresar un número.")
