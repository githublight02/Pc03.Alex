def frac(x, y):
    P = round((x / y) * 100)
    if P < 1:
        return 'E'
    elif P > 99:
        return 'F'
    else:
        return f'El combustible está al {P}%'

def datos():
    while True:
        try:
            n = input('Ingrese una fracción x/y : ')
            nume, deno = map(int, n.split('/'))
            if deno == 0:
                raise ZeroDivisionError('"y" no puede ser 0, intente de nuevo....')
            if nume <= deno:
                R = frac(nume, deno)
                print(R)
            elif nume > deno:
                print('El numerador debe ser menor o igual al denominador, intente de nuevo....')
        
        except ZeroDivisionError as e:
            print(e)
        except ValueError:
            print('Los datos no son correctos. Intente de nuevo...')

datos()


