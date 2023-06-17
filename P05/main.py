import cadena_numero as y

def main():
  while True:
    print('Se mostrarán 20 números de manera aleatoria cada vez que escriba "yes"')
    conf = input('¿Desea generar 20 números aleatorios del 0 al 100? (yes/no): ')
    conf = conf.lower()

    if conf == 'yes':
        y.cantidad_numero_aleatorios(20)  
    else:
     break
main()
