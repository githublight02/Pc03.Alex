import operaciones

def main():
    print("Calculadora básica")
    
    print("1) Suma")
    print("2) Resta")
    print("3) Producto")
    print("4) División")
    opcion = input("Seleccione una opción: ")

    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))

    if opcion == "1":
        resultado = operaciones.suma(a, b)
        if resultado is not None:
            print(f"El resultado de la suma es: {resultado}")
    elif opcion == "2":
        resultado = operaciones.resta(a, b)
        if resultado is not None:
            print(f"El resultado de la resta es: {resultado}")
    elif opcion == "3":
        resultado = operaciones.producto(a, b)
        if resultado is not None:
            print(f"El resultado del producto es: {resultado}")
    elif opcion == "4":
        resultado = operaciones.division(a, b)
        if resultado is not None:
            print(f"El resultado de la división es: {resultado}")
    else:
        print("Opción inválida.")

if __name__ == "__main__":
 main()
