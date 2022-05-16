# Ejercicio con todo lo aprendido hasta el momento

playlist = {}
playlist['Canciones'] = [] # Lista para agregar canciones

def app():

    agregar_playlist = True
    while agregar_playlist:
        nombre_playlis = input('Ingresa el nombre de la playlist: \r\n')
        if( nombre_playlis == ''):
            print('Debes agregarle un nombre a la playlist')
        else:
            playlist['Nombre'] = nombre_playlis
            agregar_playlist = False

            # Mandar a llamar la funcion para agregar las canciones
            agregar_canciones()

def agregar_canciones():
    agregar_cancion = True
    while agregar_cancion:
        nombre_playlis = playlist['Nombre']
        pregunta = f'Agrega canciones a la playlist {nombre_playlis} \r\n'
        pregunta += 'Escribe "X" para guardar la playlist \r\n'

        cancion = input(pregunta)

        if(cancion == 'x'):
            # Salir del programa
            agregar_cancion = False

            # Mostrar Resumen de la playlist
            mostrar_resumen()
        else:
            # Agregar las canciones 
            playlist['Canciones'].append(cancion)

def mostrar_resumen():
    print(f'El nombre de tu playlist es {playlist["Nombre"]} \r\n')

    print('Las canciones de tu playlist son: ')
    for cancion in playlist['Canciones']:
        print(f'{cancion}')
app()