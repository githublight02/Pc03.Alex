def ingresar_notas(m):
    notas = []
    for i in range(1, m + 1):
        while True:
            try:
                n = int(input(f"Ingrese la nota #{i} en el rango de (0-20): "))
                if n < 0 or n > 20:
                    print('La nota está fuera del rango permitido. Inténtelo de nuevo')
                else:
                    notas.append(n)
                    break
            except ValueError:
                print("La nota ingresada no es válida. Inténtelo de nuevo...")

    return notas

notas_alumno = []
m = int(input("Ingrese la cantidad de notas a ingresar: "))
notas_alumno = ingresar_notas(m)
print(f'Las notas se mostrarán en el mismo orden ingresado:\n{notas_alumno}')
