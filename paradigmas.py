def obtener_datos():
    print("Cálculo del área de un rectángulo")
    print("Ingrese los valores en unidades (por ejemplo: 5, 10)")

    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))

    return base, altura


def calcular_area_rectangulo(base, altura):
    return base * altura


def mostrar_resultado(base, altura, area):
    print(f"El área del rectángulo con base {base} y altura {altura} es: {area}")


# Programa principal
base, altura = obtener_datos()
area = calcular_area_rectangulo(base, altura)
mostrar_resultado(base, altura, area)


