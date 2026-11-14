from operaciones import (
    suma, resta, multiplicacion, division, potencia,
    modulo, raiz_cuadrada, porcentaje, valor_absoluto,
    factorial, promedio, redondeo, validar_numero
)

historial = []


def pedir_numero(mensaje):
    while True:
        numero = validar_numero(input(mensaje))
        if numero is not None:
            return numero
        print("Error: ingresa un numero valido.")


def pedir_entero(mensaje):
    while True:
        numero = pedir_numero(mensaje)
        if numero.is_integer():
            return int(numero)
        print("Error: debes ingresar un numero entero.")


def mostrar_menu():
    print("\n===== CALCULADORA =====")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Modulo")
    print("7. Raiz cuadrada")
    print("8. Porcentaje")
    print("9. Valor absoluto")
    print("10. Factorial")
    print("11. Promedio")
    print("12. Redondeo")
    print("13. Ver historial")
    print("14. Borrar historial")
    print("0. Salir")


def ejecutar_operacion(opcion):
    if opcion == 11:
        cantidad = pedir_entero("Cuantos numeros deseas ingresar: ")
        if cantidad <= 0:
            print("Debes ingresar al menos un numero.")
            return
        numeros = []
        for i in range(cantidad):
            numeros.append(pedir_numero(f"Numero {i + 1}: "))
        resultado = promedio(numeros)
        descripcion = f"Promedio de {numeros}"

    elif opcion in (7, 9, 10):
        if opcion == 10:
            numero = pedir_entero("Ingresa un numero entero: ")
            resultado = factorial(numero)
            descripcion = f"Factorial de {numero}"
        else:
            numero = pedir_numero("Ingresa un numero: ")
            if opcion == 7:
                resultado = raiz_cuadrada(numero)
                descripcion = f"Raiz cuadrada de {numero}"
            else:
                resultado = valor_absoluto(numero)
                descripcion = f"Valor absoluto de {numero}"

    elif opcion == 12:
        numero = pedir_numero("Ingresa un numero: ")
        decimales = pedir_entero("Cantidad de decimales: ")
        resultado = redondeo(numero, decimales)
        descripcion = f"Redondeo de {numero} a {decimales} decimales"

    else:
        a = pedir_numero("Primer numero: ")
        b = pedir_numero("Segundo numero: ")

        operaciones = {
            1: ("Suma", suma),
            2: ("Resta", resta),
            3: ("Multiplicacion", multiplicacion),
            4: ("Division", division),
            5: ("Potencia", potencia),
            6: ("Modulo", modulo),
            8: ("Porcentaje", porcentaje)
        }

        nombre, funcion = operaciones[opcion]
        resultado = funcion(a, b)
        descripcion = f"{nombre}: {a} y {b}"

    print("Resultado:", resultado)
    historial.append(f"{descripcion} = {resultado}")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()

        if not opcion.isdigit():
            print("Opcion no valida.")
            continue

        opcion = int(opcion)

        if opcion == 0:
            print("Gracias por usar la calculadora.")
            break

        elif opcion == 13:
            if historial:
                print("\n===== HISTORIAL =====")
                for operacion in historial:
                    print(operacion)
            else:
                print("El historial esta vacio.")

        elif opcion == 14:
            historial.clear()
            print("Historial eliminado correctamente.")

        elif 1 <= opcion <= 12:
            ejecutar_operacion(opcion)

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
