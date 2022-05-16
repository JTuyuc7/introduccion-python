# Diccionarios en python

cancion = {
    'Artista' : 'Adele',
    'Cancion' : 'Hello',
    'Lanzamiento' : 2012,
    'Album' : '21',
    'Likes': 35045315249,

}

print(cancion['Artista'])

# Mezclar datos de un diccionario con string
print(f'Album {cancion["Album"]}')

# Agregar nuevo valor
cancion['Playlist'] = 'Album 21 Adele'
print(cancion)

# Reemplazar valores
cancion['Cancion'] = 'Turning tables'
print(cancion)

# Eliminar valores
del cancion['Playlist']
print(cancion)