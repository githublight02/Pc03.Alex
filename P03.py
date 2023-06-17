def triángulo_pascal(n):
    
    triángulo = [[1]]
    
    for i in range(1, n):
        fila_actual = [1]  
        fila_anterior = triángulo[i - 1]          
        
        for j in range(1, i):
            elemento = fila_anterior[j - 1] + fila_anterior[j]
            fila_actual.append(elemento)
        
        fila_actual.append(1)  
        triángulo.append(fila_actual)    
    
    for fila in triángulo:
        print(" ".join(map(str, fila)))

n = int(input("Ingrese el número de filas del triángulo de Pascal: "))
triángulo_pascal(n)
