# Leyendo datos del usuariio usando Input

nombre = input('Ingresa tu nombre: \r\n') # \r\n Para agregar un salto de linea
print(f'Hola {nombre} ')

edad = input('Cantos años tienes: \r\n')

# Convertir un string a un entero en Python
edad = int(edad)

if (edad > 18 ):
    print('Bienvenido, puedes entrar')
else:
    print('Lo siento, no puedes ingresar')

# Mezclar entrada de datos con operadores
numero = input('Agrega un numero y veremos si es par o no: \r\n')
numero = int(numero)
if( numero % 2 == 0):
    print(f'El numero {str(numero)} es par')
else:
    print(f'El numero {str(numero)} es inpar')