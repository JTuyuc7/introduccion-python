# While y for en Python

pregunta = 'Ingresa un numero para saber si es par o impar: \r\n'
pregunta += ' (Escribe "Cerrar" para salir de la aplicacion) \r\n'
preguntar = True
while preguntar:
    numero = input(pregunta)
    if (numero == 'cerrar'):
        preguntar = False
    else:
        numero = int(numero)
        if( numero % 2 == 0):
            print(f'El numero {str(numero)} es par')
        else:
            print(f'El numero {str(numero)} es Impar')
