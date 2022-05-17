# Manejando Archivos en Python

def app():
    # Crear un archivo en python
    archivo = open('archivo.txt', 'w')

    # Generar lineas en el archivo creado
    for i in range(0,20):
        archivo.write('Esta es la linea numero ' + str(i) + '\r\n')

    # Cerrar el archivo
    archivo.close()

app()