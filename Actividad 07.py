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
def calcular_promedio_notas(suma, cantidad):
    if cantidad != 0:
        resultado = suma/cantidad
    else:
        resultado = 0
    return resultado
def contar_frcuencia(numeros):
    frequency = {}
    for numero in numeros:
        if numero in frequency:
            frequency[numero] +=1
        else:
            frequency[numero] =1
    return frequency
def sumar(a,b):
    return a+b
def restar(a,b):
    return a-b
def dividir_(a,b):
    return a/b
def multiplicar(a,b):
    return a*b
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
        case "4":
            print("\n --Calculo de promedio de calificaciones--")
            calificacion = int(input("Ingrese el numero de calificaciones que se va a calcular "))
            adittion = 0
            mayor_a_85 =0
            menor_a_60 =0
            for i in range(calificacion):
                notas = float(input("Ingrese sus notas "))
                adittion += notas
                if notas >=85:
                    mayor_a_85 +=1
                elif notas <60:
                    menor_a_60 +=1
            print(f"el promedio es: {calcular_promedio_notas(adittion,calificacion)}")
            print(f"Los mayores a 85 son: {mayor_a_85}")
            print(f"Los menores a 60 son: {menor_a_60}")
        case "5":
            print("\n --lista de n numeros--")
            cantidad = int(input("Ingrese la cantidad de numeros que se van a mostrar "))
            numeros = []
            for i in range(cantidad):
                numero = int(input("Ingrese los numeros "))
                numeros.append(numero)
                mayor =max(numeros)
                menor = min(numeros)
                frecuencias = contar_frcuencia(numeros)
                print(f"Numero mayor {mayor}")
                print(f"numero menor {menor}")
                print("Frrecuencia de los numeros ingresados: ")
                for num, freq in frecuencias.items():
                    if freq > 1:
                        print(f"  El número {num} se repite {freq} veces.")
        case "6":
            while True:
                print("\n --CALCULADORA--")
                print("1. Suma")
                print("2. Resta ")
                print("3. Multiplicacio")
                print("4. Division ")
                print("5. Volver al menu principal")
                sub_option = input("Que operacion desea realizar (1-5)")
                match sub_option:
                    case "1":
                        a = float(input("Ingrese el primer valor "))
                        b = float(input("Ingrese el segundo valor "))
                        print(f"La suma de los numeros es: {sumar(a,b)}")
                    case "2":
                         a = float(input("Ingrese el primer valor "))
                         b = float(input("Ingrese el segundo valor "))
                         print(f"El resultado de la resta es: {restar(a,b)}")
                    case "3":
                        a = float(input("Ingrese el primer valor "))
                        b = float(input("Ingrese el segundo valor "))
                        print(f"El resultado de la mutiplicacion es: {multiplicar(a,b)}")
                    case "4":
                        a = float(input("Ingrese el primer valor "))
                        b = float(input("Ingrese el segundo valor "))
                        print(f"El resultado de la division es: {dividir_(a,b)}")
                    case "5":
                        print("Volviendo al menu... Gracias por usar la calculadora")
                        break
        case "7":
            print("Gracias por utilizar nuestro programa")
            break