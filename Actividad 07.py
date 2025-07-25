def saludar():
    print("Bienvenido al Programa de operaciones matematicas")
saludar()
while True:
    print("\n ===MENU===")
    print("1. Ingreso de lista de n numeros y mostrar")
    print("2. Calcular el area y perimetro de un recvtangulo")
    print("3 Verificar si un numero ingresado es primo o no ")
    print("4. Calcular el promedio de n calificaciones y clacificar")
    print("5. Ingresar una lista de n numeros y mostrar")
    print("6. Calculadora de operaciones basicas")
    print("7. Salir")
    option = input("Que operacion desea realizar (1-7)")
    match option:
