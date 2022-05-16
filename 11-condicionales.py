# Trabajar con condiciones en Python

balance = 100
if balance > 100:
    print('Puedes pagar, adelante')
else:
    print('No puedes pagar, lo siento')


# Validar condiciones exactas
likes = 200
if(likes == 200):
    print('Excelente, muy buen contenido')

# Usano >=
comments = 500
if(comments >= 500):
    print('Super, que buenos comentarios')
else:
    print('Casi llegas a los comentarios')

lenguaje = 'Python'
if(lenguaje == 'Python'):
    print('Muy buen lenguaje de programacion')

lenguaje2 = 'Python'
if not (lenguaje == 'PHP'):
    print('No es el lenguaje seleccionado')

autenticado = False
if(autenticado == True):
    print('Usuario autenticado correctamente')
else: 
    print('Por favor inicia sesion')

# Validando condicionales anidados
lenguajes = ['Python', 'Kotlin', 'Javascript', 'Java']

if 'PHP' in lenguajes:
    print('PHP si existe')
else:
    print('PHP no forma parte de la lista')

# If anidados
autenticado = True
admin = True
if(autenticado == True):
    if (admin == True):
        print('Acceso total al sistema')
    else:
        print('Acceso parcial')
else: 
    print('Por favor inicia sesion')