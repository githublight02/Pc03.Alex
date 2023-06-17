def longitud_ultima_palabra(string):
    try:
        string = string.strip()
        palabras = string.split()
        
        if len(palabras) > 0:
            ultima_palabra = palabras[-1]
            return len(ultima_palabra)
        
        return 0
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return -1

texto = input("Ingrese un texto: ")
longitud = longitud_ultima_palabra(texto)
if longitud != -1:
    print(f"La longitud de la última palabra es: {longitud}")
