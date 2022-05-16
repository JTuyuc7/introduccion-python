# Iniciar un diccionario Vacio en Python

jugador = {}

print(f'Informacion jugador {jugador}')

# Agregar informacion al diccionario
jugador['Nombre'] = 'James'
jugador['Puntaje'] = 0
print(f'Nuevo jugador {jugador}')

# Incrementar valores en diccionarios
jugador['Puntaje'] = 800
print(f'Nuevo puntaje {jugador}')

# Acceder a un valore
print(jugador.get('consola', 'No se encuentra el valor seleccionado'))

# Iterar en un diccionario en Python usando Items en python
for llave, valor in jugador.items():
    print(f'Llave {llave} y su valor {valor}')

# Eliminar datos de un diccionario
del jugador['Nombre']
del jugador['Puntaje']

print(f'Datos del diccionario {jugador}')
